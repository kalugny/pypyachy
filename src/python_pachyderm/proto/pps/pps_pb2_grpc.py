# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from pps import pps_pb2 as pps_dot_pps__pb2


class APIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateJob = channel.unary_unary(
        '/pps.API/CreateJob',
        request_serializer=pps_dot_pps__pb2.CreateJobRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.Job.FromString,
        )
    self.InspectJob = channel.unary_unary(
        '/pps.API/InspectJob',
        request_serializer=pps_dot_pps__pb2.InspectJobRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.JobInfo.FromString,
        )
    self.ListJob = channel.unary_stream(
        '/pps.API/ListJob',
        request_serializer=pps_dot_pps__pb2.ListJobRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.JobInfo.FromString,
        )
    self.FlushJob = channel.unary_stream(
        '/pps.API/FlushJob',
        request_serializer=pps_dot_pps__pb2.FlushJobRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.JobInfo.FromString,
        )
    self.DeleteJob = channel.unary_unary(
        '/pps.API/DeleteJob',
        request_serializer=pps_dot_pps__pb2.DeleteJobRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StopJob = channel.unary_unary(
        '/pps.API/StopJob',
        request_serializer=pps_dot_pps__pb2.StopJobRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InspectDatum = channel.unary_unary(
        '/pps.API/InspectDatum',
        request_serializer=pps_dot_pps__pb2.InspectDatumRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.DatumInfo.FromString,
        )
    self.ListDatum = channel.unary_stream(
        '/pps.API/ListDatum',
        request_serializer=pps_dot_pps__pb2.ListDatumRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.DatumInfo.FromString,
        )
    self.RestartDatum = channel.unary_unary(
        '/pps.API/RestartDatum',
        request_serializer=pps_dot_pps__pb2.RestartDatumRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CreatePipeline = channel.unary_unary(
        '/pps.API/CreatePipeline',
        request_serializer=pps_dot_pps__pb2.CreatePipelineRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.InspectPipeline = channel.unary_unary(
        '/pps.API/InspectPipeline',
        request_serializer=pps_dot_pps__pb2.InspectPipelineRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.PipelineInfo.FromString,
        )
    self.ListPipeline = channel.unary_unary(
        '/pps.API/ListPipeline',
        request_serializer=pps_dot_pps__pb2.ListPipelineRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.PipelineInfos.FromString,
        )
    self.DeletePipeline = channel.unary_unary(
        '/pps.API/DeletePipeline',
        request_serializer=pps_dot_pps__pb2.DeletePipelineRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StartPipeline = channel.unary_unary(
        '/pps.API/StartPipeline',
        request_serializer=pps_dot_pps__pb2.StartPipelineRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StopPipeline = channel.unary_unary(
        '/pps.API/StopPipeline',
        request_serializer=pps_dot_pps__pb2.StopPipelineRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.RunPipeline = channel.unary_unary(
        '/pps.API/RunPipeline',
        request_serializer=pps_dot_pps__pb2.RunPipelineRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.RunCron = channel.unary_unary(
        '/pps.API/RunCron',
        request_serializer=pps_dot_pps__pb2.RunCronRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CreateSecret = channel.unary_unary(
        '/pps.API/CreateSecret',
        request_serializer=pps_dot_pps__pb2.CreateSecretRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteSecret = channel.unary_unary(
        '/pps.API/DeleteSecret',
        request_serializer=pps_dot_pps__pb2.DeleteSecretRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListSecret = channel.unary_unary(
        '/pps.API/ListSecret',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.SecretInfos.FromString,
        )
    self.InspectSecret = channel.unary_unary(
        '/pps.API/InspectSecret',
        request_serializer=pps_dot_pps__pb2.InspectSecretRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.SecretInfo.FromString,
        )
    self.DeleteAll = channel.unary_unary(
        '/pps.API/DeleteAll',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetLogs = channel.unary_stream(
        '/pps.API/GetLogs',
        request_serializer=pps_dot_pps__pb2.GetLogsRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.LogMessage.FromString,
        )
    self.ActivateAuth = channel.unary_unary(
        '/pps.API/ActivateAuth',
        request_serializer=pps_dot_pps__pb2.ActivateAuthRequest.SerializeToString,
        response_deserializer=pps_dot_pps__pb2.ActivateAuthResponse.FromString,
        )
    self.UpdateJobState = channel.unary_unary(
        '/pps.API/UpdateJobState',
        request_serializer=pps_dot_pps__pb2.UpdateJobStateRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class APIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListJob(self, request, context):
    """ListJob returns information about current and past Pachyderm jobs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FlushJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectDatum(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListDatum(self, request, context):
    """ListDatum returns information about each datum fed to a Pachyderm job
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestartDatum(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreatePipeline(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectPipeline(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPipeline(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePipeline(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartPipeline(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopPipeline(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunPipeline(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunCron(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateSecret(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSecret(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListSecret(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InspectSecret(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAll(self, request, context):
    """DeleteAll deletes everything
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLogs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ActivateAuth(self, request, context):
    """An internal call that causes PPS to put itself into an auth-enabled state
    (all pipeline have tokens, correct permissions, etcd)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateJobState(self, request, context):
    """An internal call used to move a job from one state to another
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateJob': grpc.unary_unary_rpc_method_handler(
          servicer.CreateJob,
          request_deserializer=pps_dot_pps__pb2.CreateJobRequest.FromString,
          response_serializer=pps_dot_pps__pb2.Job.SerializeToString,
      ),
      'InspectJob': grpc.unary_unary_rpc_method_handler(
          servicer.InspectJob,
          request_deserializer=pps_dot_pps__pb2.InspectJobRequest.FromString,
          response_serializer=pps_dot_pps__pb2.JobInfo.SerializeToString,
      ),
      'ListJob': grpc.unary_stream_rpc_method_handler(
          servicer.ListJob,
          request_deserializer=pps_dot_pps__pb2.ListJobRequest.FromString,
          response_serializer=pps_dot_pps__pb2.JobInfo.SerializeToString,
      ),
      'FlushJob': grpc.unary_stream_rpc_method_handler(
          servicer.FlushJob,
          request_deserializer=pps_dot_pps__pb2.FlushJobRequest.FromString,
          response_serializer=pps_dot_pps__pb2.JobInfo.SerializeToString,
      ),
      'DeleteJob': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteJob,
          request_deserializer=pps_dot_pps__pb2.DeleteJobRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StopJob': grpc.unary_unary_rpc_method_handler(
          servicer.StopJob,
          request_deserializer=pps_dot_pps__pb2.StopJobRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InspectDatum': grpc.unary_unary_rpc_method_handler(
          servicer.InspectDatum,
          request_deserializer=pps_dot_pps__pb2.InspectDatumRequest.FromString,
          response_serializer=pps_dot_pps__pb2.DatumInfo.SerializeToString,
      ),
      'ListDatum': grpc.unary_stream_rpc_method_handler(
          servicer.ListDatum,
          request_deserializer=pps_dot_pps__pb2.ListDatumRequest.FromString,
          response_serializer=pps_dot_pps__pb2.DatumInfo.SerializeToString,
      ),
      'RestartDatum': grpc.unary_unary_rpc_method_handler(
          servicer.RestartDatum,
          request_deserializer=pps_dot_pps__pb2.RestartDatumRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CreatePipeline': grpc.unary_unary_rpc_method_handler(
          servicer.CreatePipeline,
          request_deserializer=pps_dot_pps__pb2.CreatePipelineRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'InspectPipeline': grpc.unary_unary_rpc_method_handler(
          servicer.InspectPipeline,
          request_deserializer=pps_dot_pps__pb2.InspectPipelineRequest.FromString,
          response_serializer=pps_dot_pps__pb2.PipelineInfo.SerializeToString,
      ),
      'ListPipeline': grpc.unary_unary_rpc_method_handler(
          servicer.ListPipeline,
          request_deserializer=pps_dot_pps__pb2.ListPipelineRequest.FromString,
          response_serializer=pps_dot_pps__pb2.PipelineInfos.SerializeToString,
      ),
      'DeletePipeline': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePipeline,
          request_deserializer=pps_dot_pps__pb2.DeletePipelineRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StartPipeline': grpc.unary_unary_rpc_method_handler(
          servicer.StartPipeline,
          request_deserializer=pps_dot_pps__pb2.StartPipelineRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StopPipeline': grpc.unary_unary_rpc_method_handler(
          servicer.StopPipeline,
          request_deserializer=pps_dot_pps__pb2.StopPipelineRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'RunPipeline': grpc.unary_unary_rpc_method_handler(
          servicer.RunPipeline,
          request_deserializer=pps_dot_pps__pb2.RunPipelineRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'RunCron': grpc.unary_unary_rpc_method_handler(
          servicer.RunCron,
          request_deserializer=pps_dot_pps__pb2.RunCronRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CreateSecret': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSecret,
          request_deserializer=pps_dot_pps__pb2.CreateSecretRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteSecret': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSecret,
          request_deserializer=pps_dot_pps__pb2.DeleteSecretRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListSecret': grpc.unary_unary_rpc_method_handler(
          servicer.ListSecret,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=pps_dot_pps__pb2.SecretInfos.SerializeToString,
      ),
      'InspectSecret': grpc.unary_unary_rpc_method_handler(
          servicer.InspectSecret,
          request_deserializer=pps_dot_pps__pb2.InspectSecretRequest.FromString,
          response_serializer=pps_dot_pps__pb2.SecretInfo.SerializeToString,
      ),
      'DeleteAll': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAll,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetLogs': grpc.unary_stream_rpc_method_handler(
          servicer.GetLogs,
          request_deserializer=pps_dot_pps__pb2.GetLogsRequest.FromString,
          response_serializer=pps_dot_pps__pb2.LogMessage.SerializeToString,
      ),
      'ActivateAuth': grpc.unary_unary_rpc_method_handler(
          servicer.ActivateAuth,
          request_deserializer=pps_dot_pps__pb2.ActivateAuthRequest.FromString,
          response_serializer=pps_dot_pps__pb2.ActivateAuthResponse.SerializeToString,
      ),
      'UpdateJobState': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateJobState,
          request_deserializer=pps_dot_pps__pb2.UpdateJobStateRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pps.API', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
