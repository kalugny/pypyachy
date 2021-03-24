# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from python_pachyderm.proto.enterprise import enterprise_pb2 as src_dot_enterprise_dot_enterprise__pb2


class APIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Activate = channel.unary_unary(
        '/enterprise.API/Activate',
        request_serializer=src_dot_enterprise_dot_enterprise__pb2.ActivateRequest.SerializeToString,
        response_deserializer=src_dot_enterprise_dot_enterprise__pb2.ActivateResponse.FromString,
        )
    self.GetState = channel.unary_unary(
        '/enterprise.API/GetState',
        request_serializer=src_dot_enterprise_dot_enterprise__pb2.GetStateRequest.SerializeToString,
        response_deserializer=src_dot_enterprise_dot_enterprise__pb2.GetStateResponse.FromString,
        )
    self.GetActivationCode = channel.unary_unary(
        '/enterprise.API/GetActivationCode',
        request_serializer=src_dot_enterprise_dot_enterprise__pb2.GetActivationCodeRequest.SerializeToString,
        response_deserializer=src_dot_enterprise_dot_enterprise__pb2.GetActivationCodeResponse.FromString,
        )
    self.Heartbeat = channel.unary_unary(
        '/enterprise.API/Heartbeat',
        request_serializer=src_dot_enterprise_dot_enterprise__pb2.HeartbeatRequest.SerializeToString,
        response_deserializer=src_dot_enterprise_dot_enterprise__pb2.HeartbeatResponse.FromString,
        )
    self.GetActivationCode = channel.unary_unary(
        '/enterprise.API/GetActivationCode',
        request_serializer=client_dot_enterprise_dot_enterprise__pb2.GetActivationCodeRequest.SerializeToString,
        response_deserializer=client_dot_enterprise_dot_enterprise__pb2.GetActivationCodeResponse.FromString,
        )
    self.Deactivate = channel.unary_unary(
        '/enterprise.API/Deactivate',
        request_serializer=src_dot_enterprise_dot_enterprise__pb2.DeactivateRequest.SerializeToString,
        response_deserializer=src_dot_enterprise_dot_enterprise__pb2.DeactivateResponse.FromString,
        )


class APIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Activate(self, request, context):
    """Provide a Pachyderm enterprise token, enabling Pachyderm enterprise
    features, such as the Pachyderm Dashboard and Auth system
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetActivationCode(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Heartbeat(self, request, context):
    """Heartbeat is used in testing to trigger a heartbeat on demand. Normally this happens
    on a timer.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Deactivate(self, request, context):
    """Deactivate removes a cluster's enterprise activation
    token and sets its enterprise state to NONE.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Activate': grpc.unary_unary_rpc_method_handler(
          servicer.Activate,
          request_deserializer=src_dot_enterprise_dot_enterprise__pb2.ActivateRequest.FromString,
          response_serializer=src_dot_enterprise_dot_enterprise__pb2.ActivateResponse.SerializeToString,
      ),
      'GetState': grpc.unary_unary_rpc_method_handler(
          servicer.GetState,
          request_deserializer=src_dot_enterprise_dot_enterprise__pb2.GetStateRequest.FromString,
          response_serializer=src_dot_enterprise_dot_enterprise__pb2.GetStateResponse.SerializeToString,
      ),
      'GetActivationCode': grpc.unary_unary_rpc_method_handler(
          servicer.GetActivationCode,
          request_deserializer=src_dot_enterprise_dot_enterprise__pb2.GetActivationCodeRequest.FromString,
          response_serializer=src_dot_enterprise_dot_enterprise__pb2.GetActivationCodeResponse.SerializeToString,
      ),
      'Heartbeat': grpc.unary_unary_rpc_method_handler(
          servicer.Heartbeat,
          request_deserializer=src_dot_enterprise_dot_enterprise__pb2.HeartbeatRequest.FromString,
          response_serializer=src_dot_enterprise_dot_enterprise__pb2.HeartbeatResponse.SerializeToString,
      ),
      'GetActivationCode': grpc.unary_unary_rpc_method_handler(
          servicer.GetActivationCode,
          request_deserializer=client_dot_enterprise_dot_enterprise__pb2.GetActivationCodeRequest.FromString,
          response_serializer=client_dot_enterprise_dot_enterprise__pb2.GetActivationCodeResponse.SerializeToString,
      ),
      'Deactivate': grpc.unary_unary_rpc_method_handler(
          servicer.Deactivate,
          request_deserializer=src_dot_enterprise_dot_enterprise__pb2.DeactivateRequest.FromString,
          response_serializer=src_dot_enterprise_dot_enterprise__pb2.DeactivateResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'enterprise.API', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
