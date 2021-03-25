# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/server/pfs/server/pfsserver.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/server/pfs/server/pfsserver.proto',
  package='pfsserver',
  syntax='proto3',
  serialized_options=b'Z7github.com/pachyderm/pachyderm/v2/src/server/pfs/server',
  serialized_pb=b'\n%src/server/pfs/server/pfsserver.proto\x12\tpfsserver\"E\n\x0e\x43ompactionTask\x12\x0e\n\x06inputs\x18\x01 \x03(\t\x12#\n\x05range\x18\x02 \x01(\x0b\x32\x14.pfsserver.PathRange\"\"\n\x14\x43ompactionTaskResult\x12\n\n\x02id\x18\x01 \x01(\t\")\n\tPathRange\x12\r\n\x05lower\x18\x01 \x01(\t\x12\r\n\x05upper\x18\x02 \x01(\tB9Z7github.com/pachyderm/pachyderm/v2/src/server/pfs/serverb\x06proto3'
)




_COMPACTIONTASK = _descriptor.Descriptor(
  name='CompactionTask',
  full_name='pfsserver.CompactionTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='pfsserver.CompactionTask.inputs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='pfsserver.CompactionTask.range', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=52,
  serialized_end=121,
)


_COMPACTIONTASKRESULT = _descriptor.Descriptor(
  name='CompactionTaskResult',
  full_name='pfsserver.CompactionTaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pfsserver.CompactionTaskResult.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=123,
  serialized_end=157,
)


_PATHRANGE = _descriptor.Descriptor(
  name='PathRange',
  full_name='pfsserver.PathRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lower', full_name='pfsserver.PathRange.lower', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upper', full_name='pfsserver.PathRange.upper', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=159,
  serialized_end=200,
)

_COMPACTIONTASK.fields_by_name['range'].message_type = _PATHRANGE
DESCRIPTOR.message_types_by_name['CompactionTask'] = _COMPACTIONTASK
DESCRIPTOR.message_types_by_name['CompactionTaskResult'] = _COMPACTIONTASKRESULT
DESCRIPTOR.message_types_by_name['PathRange'] = _PATHRANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CompactionTask = _reflection.GeneratedProtocolMessageType('CompactionTask', (_message.Message,), {
  'DESCRIPTOR' : _COMPACTIONTASK,
  '__module__' : 'src.server.pfs.server.pfsserver_pb2'
  # @@protoc_insertion_point(class_scope:pfsserver.CompactionTask)
  })
_sym_db.RegisterMessage(CompactionTask)

CompactionTaskResult = _reflection.GeneratedProtocolMessageType('CompactionTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _COMPACTIONTASKRESULT,
  '__module__' : 'src.server.pfs.server.pfsserver_pb2'
  # @@protoc_insertion_point(class_scope:pfsserver.CompactionTaskResult)
  })
_sym_db.RegisterMessage(CompactionTaskResult)

PathRange = _reflection.GeneratedProtocolMessageType('PathRange', (_message.Message,), {
  'DESCRIPTOR' : _PATHRANGE,
  '__module__' : 'src.server.pfs.server.pfsserver_pb2'
  # @@protoc_insertion_point(class_scope:pfsserver.PathRange)
  })
_sym_db.RegisterMessage(PathRange)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)