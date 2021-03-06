# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: python_pachyderm/proto/v2/enterprise/enterprise.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='python_pachyderm/proto/v2/enterprise/enterprise.proto',
  package='enterprise_v2',
  syntax='proto3',
  serialized_options=b'Z0github.com/pachyderm/pachyderm/v2/src/enterprise',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5python_pachyderm/proto/v2/enterprise/enterprise.proto\x12\renterprise_v2\x1a\x1fgoogle/protobuf/timestamp.proto\"U\n\rLicenseRecord\x12\x17\n\x0f\x61\x63tivation_code\x18\x01 \x01(\t\x12+\n\x07\x65xpires\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"F\n\x10\x45nterpriseConfig\x12\x16\n\x0elicense_server\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06secret\x18\x03 \x01(\t\"\x8f\x01\n\x10\x45nterpriseRecord\x12-\n\x07license\x18\x01 \x01(\x0b\x32\x1c.enterprise_v2.LicenseRecord\x12\x32\n\x0elast_heartbeat\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10heartbeat_failed\x18\x03 \x01(\x08\"8\n\tTokenInfo\x12+\n\x07\x65xpires\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"E\n\x0f\x41\x63tivateRequest\x12\x16\n\x0elicense_server\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06secret\x18\x03 \x01(\t\"\x12\n\x10\x41\x63tivateResponse\"\x11\n\x0fGetStateRequest\"x\n\x10GetStateResponse\x12#\n\x05state\x18\x01 \x01(\x0e\x32\x14.enterprise_v2.State\x12&\n\x04info\x18\x02 \x01(\x0b\x32\x18.enterprise_v2.TokenInfo\x12\x17\n\x0f\x61\x63tivation_code\x18\x03 \x01(\t\"\x1a\n\x18GetActivationCodeRequest\"\x81\x01\n\x19GetActivationCodeResponse\x12#\n\x05state\x18\x01 \x01(\x0e\x32\x14.enterprise_v2.State\x12&\n\x04info\x18\x02 \x01(\x0b\x32\x18.enterprise_v2.TokenInfo\x12\x17\n\x0f\x61\x63tivation_code\x18\x03 \x01(\t\"\x12\n\x10HeartbeatRequest\"\x13\n\x11HeartbeatResponse\"\x13\n\x11\x44\x65\x61\x63tivateRequest\"\x14\n\x12\x44\x65\x61\x63tivateResponse*@\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0b\n\x07\x45XPIRED\x10\x02\x12\x14\n\x10HEARTBEAT_FAILED\x10\x03\x32\xb4\x03\n\x03\x41PI\x12M\n\x08\x41\x63tivate\x12\x1e.enterprise_v2.ActivateRequest\x1a\x1f.enterprise_v2.ActivateResponse\"\x00\x12M\n\x08GetState\x12\x1e.enterprise_v2.GetStateRequest\x1a\x1f.enterprise_v2.GetStateResponse\"\x00\x12h\n\x11GetActivationCode\x12\'.enterprise_v2.GetActivationCodeRequest\x1a(.enterprise_v2.GetActivationCodeResponse\"\x00\x12P\n\tHeartbeat\x12\x1f.enterprise_v2.HeartbeatRequest\x1a .enterprise_v2.HeartbeatResponse\"\x00\x12S\n\nDeactivate\x12 .enterprise_v2.DeactivateRequest\x1a!.enterprise_v2.DeactivateResponse\"\x00\x42\x32Z0github.com/pachyderm/pachyderm/v2/src/enterpriseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='enterprise_v2.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HEARTBEAT_FAILED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=944,
  serialized_end=1008,
)
_sym_db.RegisterEnumDescriptor(_STATE)

State = enum_type_wrapper.EnumTypeWrapper(_STATE)
NONE = 0
ACTIVE = 1
EXPIRED = 2
HEARTBEAT_FAILED = 3



_LICENSERECORD = _descriptor.Descriptor(
  name='LicenseRecord',
  full_name='enterprise_v2.LicenseRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activation_code', full_name='enterprise_v2.LicenseRecord.activation_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expires', full_name='enterprise_v2.LicenseRecord.expires', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=190,
)


_ENTERPRISECONFIG = _descriptor.Descriptor(
  name='EnterpriseConfig',
  full_name='enterprise_v2.EnterpriseConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='license_server', full_name='enterprise_v2.EnterpriseConfig.license_server', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='enterprise_v2.EnterpriseConfig.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='enterprise_v2.EnterpriseConfig.secret', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=262,
)


_ENTERPRISERECORD = _descriptor.Descriptor(
  name='EnterpriseRecord',
  full_name='enterprise_v2.EnterpriseRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='license', full_name='enterprise_v2.EnterpriseRecord.license', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_heartbeat', full_name='enterprise_v2.EnterpriseRecord.last_heartbeat', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heartbeat_failed', full_name='enterprise_v2.EnterpriseRecord.heartbeat_failed', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=408,
)


_TOKENINFO = _descriptor.Descriptor(
  name='TokenInfo',
  full_name='enterprise_v2.TokenInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='expires', full_name='enterprise_v2.TokenInfo.expires', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=466,
)


_ACTIVATEREQUEST = _descriptor.Descriptor(
  name='ActivateRequest',
  full_name='enterprise_v2.ActivateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='license_server', full_name='enterprise_v2.ActivateRequest.license_server', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='enterprise_v2.ActivateRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='enterprise_v2.ActivateRequest.secret', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=537,
)


_ACTIVATERESPONSE = _descriptor.Descriptor(
  name='ActivateResponse',
  full_name='enterprise_v2.ActivateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=557,
)


_GETSTATEREQUEST = _descriptor.Descriptor(
  name='GetStateRequest',
  full_name='enterprise_v2.GetStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=576,
)


_GETSTATERESPONSE = _descriptor.Descriptor(
  name='GetStateResponse',
  full_name='enterprise_v2.GetStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='enterprise_v2.GetStateResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='enterprise_v2.GetStateResponse.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='activation_code', full_name='enterprise_v2.GetStateResponse.activation_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=698,
)


_GETACTIVATIONCODEREQUEST = _descriptor.Descriptor(
  name='GetActivationCodeRequest',
  full_name='enterprise_v2.GetActivationCodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=726,
)


_GETACTIVATIONCODERESPONSE = _descriptor.Descriptor(
  name='GetActivationCodeResponse',
  full_name='enterprise_v2.GetActivationCodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='enterprise_v2.GetActivationCodeResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='enterprise_v2.GetActivationCodeResponse.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='activation_code', full_name='enterprise_v2.GetActivationCodeResponse.activation_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=858,
)


_HEARTBEATREQUEST = _descriptor.Descriptor(
  name='HeartbeatRequest',
  full_name='enterprise_v2.HeartbeatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=860,
  serialized_end=878,
)


_HEARTBEATRESPONSE = _descriptor.Descriptor(
  name='HeartbeatResponse',
  full_name='enterprise_v2.HeartbeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=880,
  serialized_end=899,
)


_DEACTIVATEREQUEST = _descriptor.Descriptor(
  name='DeactivateRequest',
  full_name='enterprise_v2.DeactivateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=901,
  serialized_end=920,
)


_DEACTIVATERESPONSE = _descriptor.Descriptor(
  name='DeactivateResponse',
  full_name='enterprise_v2.DeactivateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=922,
  serialized_end=942,
)

_LICENSERECORD.fields_by_name['expires'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ENTERPRISERECORD.fields_by_name['license'].message_type = _LICENSERECORD
_ENTERPRISERECORD.fields_by_name['last_heartbeat'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TOKENINFO.fields_by_name['expires'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETSTATERESPONSE.fields_by_name['state'].enum_type = _STATE
_GETSTATERESPONSE.fields_by_name['info'].message_type = _TOKENINFO
_GETACTIVATIONCODERESPONSE.fields_by_name['state'].enum_type = _STATE
_GETACTIVATIONCODERESPONSE.fields_by_name['info'].message_type = _TOKENINFO
DESCRIPTOR.message_types_by_name['LicenseRecord'] = _LICENSERECORD
DESCRIPTOR.message_types_by_name['EnterpriseConfig'] = _ENTERPRISECONFIG
DESCRIPTOR.message_types_by_name['EnterpriseRecord'] = _ENTERPRISERECORD
DESCRIPTOR.message_types_by_name['TokenInfo'] = _TOKENINFO
DESCRIPTOR.message_types_by_name['ActivateRequest'] = _ACTIVATEREQUEST
DESCRIPTOR.message_types_by_name['ActivateResponse'] = _ACTIVATERESPONSE
DESCRIPTOR.message_types_by_name['GetStateRequest'] = _GETSTATEREQUEST
DESCRIPTOR.message_types_by_name['GetStateResponse'] = _GETSTATERESPONSE
DESCRIPTOR.message_types_by_name['GetActivationCodeRequest'] = _GETACTIVATIONCODEREQUEST
DESCRIPTOR.message_types_by_name['GetActivationCodeResponse'] = _GETACTIVATIONCODERESPONSE
DESCRIPTOR.message_types_by_name['HeartbeatRequest'] = _HEARTBEATREQUEST
DESCRIPTOR.message_types_by_name['HeartbeatResponse'] = _HEARTBEATRESPONSE
DESCRIPTOR.message_types_by_name['DeactivateRequest'] = _DEACTIVATEREQUEST
DESCRIPTOR.message_types_by_name['DeactivateResponse'] = _DEACTIVATERESPONSE
DESCRIPTOR.enum_types_by_name['State'] = _STATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LicenseRecord = _reflection.GeneratedProtocolMessageType('LicenseRecord', (_message.Message,), {
  'DESCRIPTOR' : _LICENSERECORD,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.LicenseRecord)
  })
_sym_db.RegisterMessage(LicenseRecord)

EnterpriseConfig = _reflection.GeneratedProtocolMessageType('EnterpriseConfig', (_message.Message,), {
  'DESCRIPTOR' : _ENTERPRISECONFIG,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.EnterpriseConfig)
  })
_sym_db.RegisterMessage(EnterpriseConfig)

EnterpriseRecord = _reflection.GeneratedProtocolMessageType('EnterpriseRecord', (_message.Message,), {
  'DESCRIPTOR' : _ENTERPRISERECORD,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.EnterpriseRecord)
  })
_sym_db.RegisterMessage(EnterpriseRecord)

TokenInfo = _reflection.GeneratedProtocolMessageType('TokenInfo', (_message.Message,), {
  'DESCRIPTOR' : _TOKENINFO,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.TokenInfo)
  })
_sym_db.RegisterMessage(TokenInfo)

ActivateRequest = _reflection.GeneratedProtocolMessageType('ActivateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATEREQUEST,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.ActivateRequest)
  })
_sym_db.RegisterMessage(ActivateRequest)

ActivateResponse = _reflection.GeneratedProtocolMessageType('ActivateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATERESPONSE,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.ActivateResponse)
  })
_sym_db.RegisterMessage(ActivateResponse)

GetStateRequest = _reflection.GeneratedProtocolMessageType('GetStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATEREQUEST,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.GetStateRequest)
  })
_sym_db.RegisterMessage(GetStateRequest)

GetStateResponse = _reflection.GeneratedProtocolMessageType('GetStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATERESPONSE,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.GetStateResponse)
  })
_sym_db.RegisterMessage(GetStateResponse)

GetActivationCodeRequest = _reflection.GeneratedProtocolMessageType('GetActivationCodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACTIVATIONCODEREQUEST,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.GetActivationCodeRequest)
  })
_sym_db.RegisterMessage(GetActivationCodeRequest)

GetActivationCodeResponse = _reflection.GeneratedProtocolMessageType('GetActivationCodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACTIVATIONCODERESPONSE,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.GetActivationCodeResponse)
  })
_sym_db.RegisterMessage(GetActivationCodeResponse)

HeartbeatRequest = _reflection.GeneratedProtocolMessageType('HeartbeatRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREQUEST,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.HeartbeatRequest)
  })
_sym_db.RegisterMessage(HeartbeatRequest)

HeartbeatResponse = _reflection.GeneratedProtocolMessageType('HeartbeatResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATRESPONSE,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.HeartbeatResponse)
  })
_sym_db.RegisterMessage(HeartbeatResponse)

DeactivateRequest = _reflection.GeneratedProtocolMessageType('DeactivateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEACTIVATEREQUEST,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.DeactivateRequest)
  })
_sym_db.RegisterMessage(DeactivateRequest)

DeactivateResponse = _reflection.GeneratedProtocolMessageType('DeactivateResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEACTIVATERESPONSE,
  '__module__' : 'python_pachyderm.proto.v2.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise_v2.DeactivateResponse)
  })
_sym_db.RegisterMessage(DeactivateResponse)


DESCRIPTOR._options = None

_API = _descriptor.ServiceDescriptor(
  name='API',
  full_name='enterprise_v2.API',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1011,
  serialized_end=1447,
  methods=[
  _descriptor.MethodDescriptor(
    name='Activate',
    full_name='enterprise_v2.API.Activate',
    index=0,
    containing_service=None,
    input_type=_ACTIVATEREQUEST,
    output_type=_ACTIVATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='enterprise_v2.API.GetState',
    index=1,
    containing_service=None,
    input_type=_GETSTATEREQUEST,
    output_type=_GETSTATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetActivationCode',
    full_name='enterprise_v2.API.GetActivationCode',
    index=2,
    containing_service=None,
    input_type=_GETACTIVATIONCODEREQUEST,
    output_type=_GETACTIVATIONCODERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Heartbeat',
    full_name='enterprise_v2.API.Heartbeat',
    index=3,
    containing_service=None,
    input_type=_HEARTBEATREQUEST,
    output_type=_HEARTBEATRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Deactivate',
    full_name='enterprise_v2.API.Deactivate',
    index=4,
    containing_service=None,
    input_type=_DEACTIVATEREQUEST,
    output_type=_DEACTIVATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_API)

DESCRIPTOR.services_by_name['API'] = _API

# @@protoc_insertion_point(module_scope)
