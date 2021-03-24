# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from python_pachyderm.proto.debug import debug_pb2 as src_dot_debug_dot_debug__pb2


class DebugStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Profile = channel.unary_stream(
        '/debug.Debug/Profile',
        request_serializer=src_dot_debug_dot_debug__pb2.ProfileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
        )
    self.Binary = channel.unary_stream(
        '/debug.Debug/Binary',
        request_serializer=src_dot_debug_dot_debug__pb2.BinaryRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
        )
    self.Dump = channel.unary_stream(
        '/debug.Debug/Dump',
        request_serializer=src_dot_debug_dot_debug__pb2.DumpRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.FromString,
        )


class DebugServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Profile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Binary(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Dump(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DebugServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Profile': grpc.unary_stream_rpc_method_handler(
          servicer.Profile,
          request_deserializer=src_dot_debug_dot_debug__pb2.ProfileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.SerializeToString,
      ),
      'Binary': grpc.unary_stream_rpc_method_handler(
          servicer.Binary,
          request_deserializer=src_dot_debug_dot_debug__pb2.BinaryRequest.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.SerializeToString,
      ),
      'Dump': grpc.unary_stream_rpc_method_handler(
          servicer.Dump,
          request_deserializer=src_dot_debug_dot_debug__pb2.DumpRequest.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.BytesValue.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'debug.Debug', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
