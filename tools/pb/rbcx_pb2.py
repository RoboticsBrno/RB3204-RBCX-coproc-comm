# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rbcx.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rbcx.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nrbcx.proto\"\xc5\x01\n\rCoprocRequest\x12\x31\n\x0bledsRequest\x18\x04 \x01(\x0b\x32\x1a.CoprocRequest.LedsRequestH\x00\x12\x37\n\x0e\x62uttonsRequest\x18\x05 \x01(\x0b\x32\x1d.CoprocRequest.ButtonsRequestH\x00\x1a+\n\x0bLedsRequest\x12\x0e\n\x06ledsOn\x18\x01 \x01(\r\x12\x0c\n\x04mask\x18\x02 \x01(\r\x1a\x10\n\x0e\x42uttonsRequestB\t\n\x07payload\"\xb6\x01\n\x0c\x43oprocStatus\x12.\n\nledsStatus\x18\x04 \x01(\x0b\x32\x18.CoprocStatus.LedsStatusH\x00\x12\x34\n\rbuttonsStatus\x18\x05 \x01(\x0b\x32\x1b.CoprocStatus.ButtonsStatusH\x00\x1a\x0c\n\nLedsStatus\x1a\'\n\rButtonsStatus\x12\x16\n\x0e\x62uttonsPressed\x18\x01 \x01(\rB\t\n\x07payloadb\x06proto3'
)




_COPROCREQUEST_LEDSREQUEST = _descriptor.Descriptor(
  name='LedsRequest',
  full_name='CoprocRequest.LedsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledsOn', full_name='CoprocRequest.LedsRequest.ledsOn', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask', full_name='CoprocRequest.LedsRequest.mask', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=140,
  serialized_end=183,
)

_COPROCREQUEST_BUTTONSREQUEST = _descriptor.Descriptor(
  name='ButtonsRequest',
  full_name='CoprocRequest.ButtonsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=185,
  serialized_end=201,
)

_COPROCREQUEST = _descriptor.Descriptor(
  name='CoprocRequest',
  full_name='CoprocRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledsRequest', full_name='CoprocRequest.ledsRequest', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buttonsRequest', full_name='CoprocRequest.buttonsRequest', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COPROCREQUEST_LEDSREQUEST, _COPROCREQUEST_BUTTONSREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='CoprocRequest.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=15,
  serialized_end=212,
)


_COPROCSTATUS_LEDSSTATUS = _descriptor.Descriptor(
  name='LedsStatus',
  full_name='CoprocStatus.LedsStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=333,
  serialized_end=345,
)

_COPROCSTATUS_BUTTONSSTATUS = _descriptor.Descriptor(
  name='ButtonsStatus',
  full_name='CoprocStatus.ButtonsStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buttonsPressed', full_name='CoprocStatus.ButtonsStatus.buttonsPressed', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=347,
  serialized_end=386,
)

_COPROCSTATUS = _descriptor.Descriptor(
  name='CoprocStatus',
  full_name='CoprocStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledsStatus', full_name='CoprocStatus.ledsStatus', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buttonsStatus', full_name='CoprocStatus.buttonsStatus', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COPROCSTATUS_LEDSSTATUS, _COPROCSTATUS_BUTTONSSTATUS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='CoprocStatus.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=215,
  serialized_end=397,
)

_COPROCREQUEST_LEDSREQUEST.containing_type = _COPROCREQUEST
_COPROCREQUEST_BUTTONSREQUEST.containing_type = _COPROCREQUEST
_COPROCREQUEST.fields_by_name['ledsRequest'].message_type = _COPROCREQUEST_LEDSREQUEST
_COPROCREQUEST.fields_by_name['buttonsRequest'].message_type = _COPROCREQUEST_BUTTONSREQUEST
_COPROCREQUEST.oneofs_by_name['payload'].fields.append(
  _COPROCREQUEST.fields_by_name['ledsRequest'])
_COPROCREQUEST.fields_by_name['ledsRequest'].containing_oneof = _COPROCREQUEST.oneofs_by_name['payload']
_COPROCREQUEST.oneofs_by_name['payload'].fields.append(
  _COPROCREQUEST.fields_by_name['buttonsRequest'])
_COPROCREQUEST.fields_by_name['buttonsRequest'].containing_oneof = _COPROCREQUEST.oneofs_by_name['payload']
_COPROCSTATUS_LEDSSTATUS.containing_type = _COPROCSTATUS
_COPROCSTATUS_BUTTONSSTATUS.containing_type = _COPROCSTATUS
_COPROCSTATUS.fields_by_name['ledsStatus'].message_type = _COPROCSTATUS_LEDSSTATUS
_COPROCSTATUS.fields_by_name['buttonsStatus'].message_type = _COPROCSTATUS_BUTTONSSTATUS
_COPROCSTATUS.oneofs_by_name['payload'].fields.append(
  _COPROCSTATUS.fields_by_name['ledsStatus'])
_COPROCSTATUS.fields_by_name['ledsStatus'].containing_oneof = _COPROCSTATUS.oneofs_by_name['payload']
_COPROCSTATUS.oneofs_by_name['payload'].fields.append(
  _COPROCSTATUS.fields_by_name['buttonsStatus'])
_COPROCSTATUS.fields_by_name['buttonsStatus'].containing_oneof = _COPROCSTATUS.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['CoprocRequest'] = _COPROCREQUEST
DESCRIPTOR.message_types_by_name['CoprocStatus'] = _COPROCSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CoprocRequest = _reflection.GeneratedProtocolMessageType('CoprocRequest', (_message.Message,), {

  'LedsRequest' : _reflection.GeneratedProtocolMessageType('LedsRequest', (_message.Message,), {
    'DESCRIPTOR' : _COPROCREQUEST_LEDSREQUEST,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocRequest.LedsRequest)
    })
  ,

  'ButtonsRequest' : _reflection.GeneratedProtocolMessageType('ButtonsRequest', (_message.Message,), {
    'DESCRIPTOR' : _COPROCREQUEST_BUTTONSREQUEST,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocRequest.ButtonsRequest)
    })
  ,
  'DESCRIPTOR' : _COPROCREQUEST,
  '__module__' : 'rbcx_pb2'
  # @@protoc_insertion_point(class_scope:CoprocRequest)
  })
_sym_db.RegisterMessage(CoprocRequest)
_sym_db.RegisterMessage(CoprocRequest.LedsRequest)
_sym_db.RegisterMessage(CoprocRequest.ButtonsRequest)

CoprocStatus = _reflection.GeneratedProtocolMessageType('CoprocStatus', (_message.Message,), {

  'LedsStatus' : _reflection.GeneratedProtocolMessageType('LedsStatus', (_message.Message,), {
    'DESCRIPTOR' : _COPROCSTATUS_LEDSSTATUS,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocStatus.LedsStatus)
    })
  ,

  'ButtonsStatus' : _reflection.GeneratedProtocolMessageType('ButtonsStatus', (_message.Message,), {
    'DESCRIPTOR' : _COPROCSTATUS_BUTTONSSTATUS,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocStatus.ButtonsStatus)
    })
  ,
  'DESCRIPTOR' : _COPROCSTATUS,
  '__module__' : 'rbcx_pb2'
  # @@protoc_insertion_point(class_scope:CoprocStatus)
  })
_sym_db.RegisterMessage(CoprocStatus)
_sym_db.RegisterMessage(CoprocStatus.LedsStatus)
_sym_db.RegisterMessage(CoprocStatus.ButtonsStatus)


# @@protoc_insertion_point(module_scope)
