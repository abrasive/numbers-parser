# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TNArchives_sos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import numbers_parser.generated.TSDArchives_sos_pb2 as TSDArchives__sos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TNArchives_sos.proto',
  package='TNSOS',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14TNArchives_sos.proto\x12\x05TNSOS\x1a\x15TSDArchives_sos.proto\"c\n\"SheetStylePropertyChangeSetArchive\x12%\n\x04\x66ill\x18\x01 \x01(\x0b\x32\x17.TSDSOS.SpecFillArchive\x12\x16\n\x0e\x66ill_undefined\x18\x02 \x01(\x08'
  ,
  dependencies=[TSDArchives__sos__pb2.DESCRIPTOR,])




_SHEETSTYLEPROPERTYCHANGESETARCHIVE = _descriptor.Descriptor(
  name='SheetStylePropertyChangeSetArchive',
  full_name='TNSOS.SheetStylePropertyChangeSetArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fill', full_name='TNSOS.SheetStylePropertyChangeSetArchive.fill', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fill_undefined', full_name='TNSOS.SheetStylePropertyChangeSetArchive.fill_undefined', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=153,
)

_SHEETSTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['fill'].message_type = TSDArchives__sos__pb2._SPECFILLARCHIVE
DESCRIPTOR.message_types_by_name['SheetStylePropertyChangeSetArchive'] = _SHEETSTYLEPROPERTYCHANGESETARCHIVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SheetStylePropertyChangeSetArchive = _reflection.GeneratedProtocolMessageType('SheetStylePropertyChangeSetArchive', (_message.Message,), {
  'DESCRIPTOR' : _SHEETSTYLEPROPERTYCHANGESETARCHIVE,
  '__module__' : 'TNArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TNSOS.SheetStylePropertyChangeSetArchive)
  })
_sym_db.RegisterMessage(SheetStylePropertyChangeSetArchive)


# @@protoc_insertion_point(module_scope)
