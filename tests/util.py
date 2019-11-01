import string
import random

import python_pachyderm

def random_string(n):
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(n))

def test_repo_name(test_name, prefix=None, suffix=None):
    prefix = "" if prefix is None else "{}-".format(prefix)
    suffix = suffix or random_string(6)
    return "{}{}-{}".format(prefix, test_name, suffix)

def create_test_repo(client, test_name, prefix=None, suffix=None):
    repo_name = test_repo_name(test_name, prefix=prefix, suffix=suffix)
    client.create_repo(repo_name, "python_pachyderm test repo for {}".format(test_name))
    return repo_name

def create_test_pipeline(client, test_name):
    repo_name_suffix = random_string(6)
    input_repo_name = create_test_repo(client, test_name, prefix="input", suffix=repo_name_suffix)
    pipeline_repo_name = test_repo_name(test_name, prefix="pipeline", suffix=repo_name_suffix)

    client.create_pipeline(
        pipeline_repo_name,
        transform=python_pachyderm.Transform(cmd=["sh"], image="alpine", stdin=["cp /pfs/{}/*.dat /pfs/out/".format(input_repo_name)]),
        input=python_pachyderm.Input(pfs=python_pachyderm.PFSInput(glob="/*", repo=input_repo_name)),
        enable_stats=True,
    )

    with client.commit(input_repo_name, 'master') as commit:
        client.put_file_bytes(commit, 'file.dat', b'DATA')

    return (commit, input_repo_name, pipeline_repo_name)
