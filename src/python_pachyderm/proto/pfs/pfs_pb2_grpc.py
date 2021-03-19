# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from pfs import pfs_pb2 as pfs_dot_pfs__pb2


class APIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateRepo = channel.unary_unary(
        '/pfs.API/CreateRepo',
        request_serializer=pfs_dot_pfs__pb2.CreateRepoRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InspectRepo = channel.unary_unary(
        '/pfs.API/InspectRepo',
        request_serializer=pfs_dot_pfs__pb2.InspectRepoRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.RepoInfo.FromString,
        )
    self.ListRepo = channel.unary_unary(
        '/pfs.API/ListRepo',
        request_serializer=pfs_dot_pfs__pb2.ListRepoRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.ListRepoResponse.FromString,
        )
    self.DeleteRepo = channel.unary_unary(
        '/pfs.API/DeleteRepo',
        request_serializer=pfs_dot_pfs__pb2.DeleteRepoRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StartCommit = channel.unary_unary(
        '/pfs.API/StartCommit',
        request_serializer=pfs_dot_pfs__pb2.StartCommitRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.Commit.FromString,
        )
    self.FinishCommit = channel.unary_unary(
        '/pfs.API/FinishCommit',
        request_serializer=pfs_dot_pfs__pb2.FinishCommitRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InspectCommit = channel.unary_unary(
        '/pfs.API/InspectCommit',
        request_serializer=pfs_dot_pfs__pb2.InspectCommitRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.CommitInfo.FromString,
        )
    self.ListCommit = channel.unary_stream(
        '/pfs.API/ListCommit',
        request_serializer=pfs_dot_pfs__pb2.ListCommitRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.CommitInfo.FromString,
        )
    self.SquashCommit = channel.unary_unary(
        '/pfs.API/SquashCommit',
        request_serializer=pfs_dot_pfs__pb2.SquashCommitRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.FlushCommit = channel.unary_stream(
        '/pfs.API/FlushCommit',
        request_serializer=pfs_dot_pfs__pb2.FlushCommitRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.CommitInfo.FromString,
        )
    self.SubscribeCommit = channel.unary_stream(
        '/pfs.API/SubscribeCommit',
        request_serializer=pfs_dot_pfs__pb2.SubscribeCommitRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.CommitInfo.FromString,
        )
    self.ClearCommit = channel.unary_unary(
        '/pfs.API/ClearCommit',
        request_serializer=pfs_dot_pfs__pb2.ClearCommitRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CreateBranch = channel.unary_unary(
        '/pfs.API/CreateBranch',
        request_serializer=pfs_dot_pfs__pb2.CreateBranchRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InspectBranch = channel.unary_unary(
        '/pfs.API/InspectBranch',
        request_serializer=pfs_dot_pfs__pb2.InspectBranchRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.BranchInfo.FromString,
        )
    self.ListBranch = channel.unary_unary(
        '/pfs.API/ListBranch',
        request_serializer=pfs_dot_pfs__pb2.ListBranchRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.BranchInfos.FromString,
        )
    self.DeleteBranch = channel.unary_unary(
        '/pfs.API/DeleteBranch',
        request_serializer=pfs_dot_pfs__pb2.DeleteBranchRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ModifyFile = channel.stream_unary(
        '/pfs.API/ModifyFile',
        request_serializer=pfs_dot_pfs__pb2.ModifyFileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CopyFile = channel.unary_unary(
        '/pfs.API/CopyFile',
        request_serializer=pfs_dot_pfs__pb2.CopyFileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetFile = channel.unary_stream(
        '/pfs.API/GetFile',
        request_serializer=pfs_dot_pfs__pb2.GetFileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
        )
    self.InspectFile = channel.unary_unary(
        '/pfs.API/InspectFile',
        request_serializer=pfs_dot_pfs__pb2.InspectFileRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.FileInfo.FromString,
        )
    self.ListFile = channel.unary_stream(
        '/pfs.API/ListFile',
        request_serializer=pfs_dot_pfs__pb2.ListFileRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.FileInfo.FromString,
        )
    self.WalkFile = channel.unary_stream(
        '/pfs.API/WalkFile',
        request_serializer=pfs_dot_pfs__pb2.WalkFileRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.FileInfo.FromString,
        )
    self.GlobFile = channel.unary_stream(
        '/pfs.API/GlobFile',
        request_serializer=pfs_dot_pfs__pb2.GlobFileRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.FileInfo.FromString,
        )
    self.DiffFile = channel.unary_stream(
        '/pfs.API/DiffFile',
        request_serializer=pfs_dot_pfs__pb2.DiffFileRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.DiffFileResponse.FromString,
        )
    self.ActivateAuth = channel.unary_unary(
        '/pfs.API/ActivateAuth',
        request_serializer=pfs_dot_pfs__pb2.ActivateAuthRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.ActivateAuthResponse.FromString,
        )
    self.DeleteAll = channel.unary_unary(
        '/pfs.API/DeleteAll',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Fsck = channel.unary_stream(
        '/pfs.API/Fsck',
        request_serializer=pfs_dot_pfs__pb2.FsckRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.FsckResponse.FromString,
        )
    self.AddFileset = channel.unary_unary(
        '/pfs.API/AddFileset',
        request_serializer=pfs_dot_pfs__pb2.AddFilesetRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetFileset = channel.unary_unary(
        '/pfs.API/GetFileset',
        request_serializer=pfs_dot_pfs__pb2.GetFilesetRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.CreateFilesetResponse.FromString,
        )
    self.CreateFileset = channel.stream_unary(
        '/pfs.API/CreateFileset',
        request_serializer=pfs_dot_pfs__pb2.ModifyFileRequest.SerializeToString,
        response_deserializer=pfs_dot_pfs__pb2.CreateFilesetResponse.FromString,
        )
    self.RenewFileset = channel.unary_unary(
        '/pfs.API/RenewFileset',
        request_serializer=pfs_dot_pfs__pb2.RenewFilesetRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class APIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateRepo(self, request, context):
    """CreateRepo creates a new repo.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectRepo(self, request, context):
    """InspectRepo returns info about a repo.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListRepo(self, request, context):
    """ListRepo returns info about all repos.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteRepo(self, request, context):
    """DeleteRepo deletes a repo.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartCommit(self, request, context):
    """StartCommit creates a new write commit from a parent commit.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FinishCommit(self, request, context):
    """FinishCommit turns a write commit into a read commit.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectCommit(self, request, context):
    """InspectCommit returns the info about a commit.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListCommit(self, request, context):
    """ListCommit returns info about all commits.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SquashCommit(self, request, context):
    """SquashCommit squashes a commit into it's parent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FlushCommit(self, request, context):
    """FlushCommit waits for downstream commits to finish.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeCommit(self, request, context):
    """SubscribeCommit subscribes for new commits on a given branch.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClearCommit(self, request, context):
    """ClearCommit removes all data from the commit.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateBranch(self, request, context):
    """CreateBranch creates a new branch.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectBranch(self, request, context):
    """InspectBranch returns info about a branch.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBranch(self, request, context):
    """ListBranch returns info about the heads of branches.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteBranch(self, request, context):
    """DeleteBranch deletes a branch; note that the commits still exist.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModifyFile(self, request_iterator, context):
    """ModifyFile performs modifications on a set of files.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CopyFile(self, request, context):
    """CopyFile copies the contents of one file to another.
    TODO: Make this a part of ModifyFile.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFile(self, request, context):
    """GetFile returns a byte stream of the contents of the file.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectFile(self, request, context):
    """InspectFile returns info about a file.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListFile(self, request, context):
    """ListFile returns info about all files.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WalkFile(self, request, context):
    """WalkFile walks over all the files under a directory, including children of children.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GlobFile(self, request, context):
    """GlobFile returns info about all files.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DiffFile(self, request, context):
    """DiffFile returns the differences between 2 paths at 2 commits.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ActivateAuth(self, request, context):
    """ActivateAuth creates a role binding for all existing repos
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAll(self, request, context):
    """DeleteAll deletes everything.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Fsck(self, request, context):
    """Fsck does a file system consistency check for pfs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddFileset(self, request, context):
    """Fileset API
    AddFileset associates a fileset with a commit
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFileset(self, request, context):
    """GetFileset returns a fileset with the data from a commit
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateFileset(self, request_iterator, context):
    """CreateFileset creates a new fileset.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RenewFileset(self, request, context):
    """RenewFileset prevents a fileset from being deleted for a set amount of time.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateRepo': grpc.unary_unary_rpc_method_handler(
          servicer.CreateRepo,
          request_deserializer=pfs_dot_pfs__pb2.CreateRepoRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InspectRepo': grpc.unary_unary_rpc_method_handler(
          servicer.InspectRepo,
          request_deserializer=pfs_dot_pfs__pb2.InspectRepoRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.RepoInfo.SerializeToString,
      ),
      'ListRepo': grpc.unary_unary_rpc_method_handler(
          servicer.ListRepo,
          request_deserializer=pfs_dot_pfs__pb2.ListRepoRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.ListRepoResponse.SerializeToString,
      ),
      'DeleteRepo': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteRepo,
          request_deserializer=pfs_dot_pfs__pb2.DeleteRepoRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StartCommit': grpc.unary_unary_rpc_method_handler(
          servicer.StartCommit,
          request_deserializer=pfs_dot_pfs__pb2.StartCommitRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.Commit.SerializeToString,
      ),
      'FinishCommit': grpc.unary_unary_rpc_method_handler(
          servicer.FinishCommit,
          request_deserializer=pfs_dot_pfs__pb2.FinishCommitRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InspectCommit': grpc.unary_unary_rpc_method_handler(
          servicer.InspectCommit,
          request_deserializer=pfs_dot_pfs__pb2.InspectCommitRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.CommitInfo.SerializeToString,
      ),
      'ListCommit': grpc.unary_stream_rpc_method_handler(
          servicer.ListCommit,
          request_deserializer=pfs_dot_pfs__pb2.ListCommitRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.CommitInfo.SerializeToString,
      ),
      'SquashCommit': grpc.unary_unary_rpc_method_handler(
          servicer.SquashCommit,
          request_deserializer=pfs_dot_pfs__pb2.SquashCommitRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'FlushCommit': grpc.unary_stream_rpc_method_handler(
          servicer.FlushCommit,
          request_deserializer=pfs_dot_pfs__pb2.FlushCommitRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.CommitInfo.SerializeToString,
      ),
      'SubscribeCommit': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeCommit,
          request_deserializer=pfs_dot_pfs__pb2.SubscribeCommitRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.CommitInfo.SerializeToString,
      ),
      'ClearCommit': grpc.unary_unary_rpc_method_handler(
          servicer.ClearCommit,
          request_deserializer=pfs_dot_pfs__pb2.ClearCommitRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CreateBranch': grpc.unary_unary_rpc_method_handler(
          servicer.CreateBranch,
          request_deserializer=pfs_dot_pfs__pb2.CreateBranchRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InspectBranch': grpc.unary_unary_rpc_method_handler(
          servicer.InspectBranch,
          request_deserializer=pfs_dot_pfs__pb2.InspectBranchRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.BranchInfo.SerializeToString,
      ),
      'ListBranch': grpc.unary_unary_rpc_method_handler(
          servicer.ListBranch,
          request_deserializer=pfs_dot_pfs__pb2.ListBranchRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.BranchInfos.SerializeToString,
      ),
      'DeleteBranch': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteBranch,
          request_deserializer=pfs_dot_pfs__pb2.DeleteBranchRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ModifyFile': grpc.stream_unary_rpc_method_handler(
          servicer.ModifyFile,
          request_deserializer=pfs_dot_pfs__pb2.ModifyFileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CopyFile': grpc.unary_unary_rpc_method_handler(
          servicer.CopyFile,
          request_deserializer=pfs_dot_pfs__pb2.CopyFileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetFile': grpc.unary_stream_rpc_method_handler(
          servicer.GetFile,
          request_deserializer=pfs_dot_pfs__pb2.GetFileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.SerializeToString,
      ),
      'InspectFile': grpc.unary_unary_rpc_method_handler(
          servicer.InspectFile,
          request_deserializer=pfs_dot_pfs__pb2.InspectFileRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.FileInfo.SerializeToString,
      ),
      'ListFile': grpc.unary_stream_rpc_method_handler(
          servicer.ListFile,
          request_deserializer=pfs_dot_pfs__pb2.ListFileRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.FileInfo.SerializeToString,
      ),
      'WalkFile': grpc.unary_stream_rpc_method_handler(
          servicer.WalkFile,
          request_deserializer=pfs_dot_pfs__pb2.WalkFileRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.FileInfo.SerializeToString,
      ),
      'GlobFile': grpc.unary_stream_rpc_method_handler(
          servicer.GlobFile,
          request_deserializer=pfs_dot_pfs__pb2.GlobFileRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.FileInfo.SerializeToString,
      ),
      'DiffFile': grpc.unary_stream_rpc_method_handler(
          servicer.DiffFile,
          request_deserializer=pfs_dot_pfs__pb2.DiffFileRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.DiffFileResponse.SerializeToString,
      ),
      'ActivateAuth': grpc.unary_unary_rpc_method_handler(
          servicer.ActivateAuth,
          request_deserializer=pfs_dot_pfs__pb2.ActivateAuthRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.ActivateAuthResponse.SerializeToString,
      ),
      'DeleteAll': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAll,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Fsck': grpc.unary_stream_rpc_method_handler(
          servicer.Fsck,
          request_deserializer=pfs_dot_pfs__pb2.FsckRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.FsckResponse.SerializeToString,
      ),
      'AddFileset': grpc.unary_unary_rpc_method_handler(
          servicer.AddFileset,
          request_deserializer=pfs_dot_pfs__pb2.AddFilesetRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetFileset': grpc.unary_unary_rpc_method_handler(
          servicer.GetFileset,
          request_deserializer=pfs_dot_pfs__pb2.GetFilesetRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.CreateFilesetResponse.SerializeToString,
      ),
      'CreateFileset': grpc.stream_unary_rpc_method_handler(
          servicer.CreateFileset,
          request_deserializer=pfs_dot_pfs__pb2.ModifyFileRequest.FromString,
          response_serializer=pfs_dot_pfs__pb2.CreateFilesetResponse.SerializeToString,
      ),
      'RenewFileset': grpc.unary_unary_rpc_method_handler(
          servicer.RenewFileset,
          request_deserializer=pfs_dot_pfs__pb2.RenewFilesetRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pfs.API', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
