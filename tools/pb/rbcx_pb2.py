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
  serialized_pb=b'\n\nrbcx.proto\"\xde\x01\n\tCoprocReq\x12%\n\x07setLeds\x18\x04 \x01(\x0b\x32\x12.CoprocReq.SetLedsH\x00\x12+\n\ngetButtons\x18\x05 \x01(\x0b\x32\x15.CoprocReq.GetButtonsH\x00\x1a.\n\x07SetLeds\x12#\n\x06ledsOn\x18\x01 \x01(\x0e\x32\x13.CoprocReq.LedsEnum\x1a\x0c\n\nGetButtons\"4\n\x08LedsEnum\x12\x08\n\x04NONE\x10\x00\x12\x06\n\x02L1\x10\x01\x12\x06\n\x02L2\x10\x02\x12\x06\n\x02L3\x10\x04\x12\x06\n\x02L4\x10\x08\x42\t\n\x07payload\"\x89\x02\n\nCoprocStat\x12(\n\x08ledsStat\x18\x04 \x01(\x0b\x32\x14.CoprocStat.LedsStatH\x00\x12.\n\x0b\x62uttonsStat\x18\x05 \x01(\x0b\x32\x17.CoprocStat.ButtonsStatH\x00\x1a\n\n\x08LedsStat\x1a>\n\x0b\x42uttonsStat\x12/\n\x0e\x62uttonsPressed\x18\x01 \x01(\x0e\x32\x17.CoprocStat.ButtonsEnum\"J\n\x0b\x42uttonsEnum\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04\x42OFF\x10\x01\x12\x06\n\x02\x42\x31\x10\x02\x12\x06\n\x02\x42\x32\x10\x04\x12\x06\n\x02\x42\x33\x10\x08\x12\x06\n\x02\x42\x34\x10\x10\x12\x07\n\x03\x42ON\x10 B\t\n\x07payloadb\x06proto3'
)



_COPROCREQ_LEDSENUM = _descriptor.EnumDescriptor(
  name='LedsEnum',
  full_name='CoprocReq.LedsEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='L1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='L2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='L3', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='L4', index=4, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=174,
  serialized_end=226,
)
_sym_db.RegisterEnumDescriptor(_COPROCREQ_LEDSENUM)

_COPROCSTAT_BUTTONSENUM = _descriptor.EnumDescriptor(
  name='ButtonsEnum',
  full_name='CoprocStat.ButtonsEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOFF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B1', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B2', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B3', index=4, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B4', index=5, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BON', index=6, number=32,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=420,
  serialized_end=494,
)
_sym_db.RegisterEnumDescriptor(_COPROCSTAT_BUTTONSENUM)


_COPROCREQ_SETLEDS = _descriptor.Descriptor(
  name='SetLeds',
  full_name='CoprocReq.SetLeds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledsOn', full_name='CoprocReq.SetLeds.ledsOn', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=112,
  serialized_end=158,
)

_COPROCREQ_GETBUTTONS = _descriptor.Descriptor(
  name='GetButtons',
  full_name='CoprocReq.GetButtons',
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
  serialized_start=160,
  serialized_end=172,
)

_COPROCREQ = _descriptor.Descriptor(
  name='CoprocReq',
  full_name='CoprocReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='setLeds', full_name='CoprocReq.setLeds', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='getButtons', full_name='CoprocReq.getButtons', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COPROCREQ_SETLEDS, _COPROCREQ_GETBUTTONS, ],
  enum_types=[
    _COPROCREQ_LEDSENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='CoprocReq.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=15,
  serialized_end=237,
)


_COPROCSTAT_LEDSSTAT = _descriptor.Descriptor(
  name='LedsStat',
  full_name='CoprocStat.LedsStat',
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
  serialized_start=344,
  serialized_end=354,
)

_COPROCSTAT_BUTTONSSTAT = _descriptor.Descriptor(
  name='ButtonsStat',
  full_name='CoprocStat.ButtonsStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buttonsPressed', full_name='CoprocStat.ButtonsStat.buttonsPressed', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=356,
  serialized_end=418,
)

_COPROCSTAT = _descriptor.Descriptor(
  name='CoprocStat',
  full_name='CoprocStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledsStat', full_name='CoprocStat.ledsStat', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buttonsStat', full_name='CoprocStat.buttonsStat', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COPROCSTAT_LEDSSTAT, _COPROCSTAT_BUTTONSSTAT, ],
  enum_types=[
    _COPROCSTAT_BUTTONSENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='CoprocStat.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=240,
  serialized_end=505,
)

_COPROCREQ_SETLEDS.fields_by_name['ledsOn'].enum_type = _COPROCREQ_LEDSENUM
_COPROCREQ_SETLEDS.containing_type = _COPROCREQ
_COPROCREQ_GETBUTTONS.containing_type = _COPROCREQ
_COPROCREQ.fields_by_name['setLeds'].message_type = _COPROCREQ_SETLEDS
_COPROCREQ.fields_by_name['getButtons'].message_type = _COPROCREQ_GETBUTTONS
_COPROCREQ_LEDSENUM.containing_type = _COPROCREQ
_COPROCREQ.oneofs_by_name['payload'].fields.append(
  _COPROCREQ.fields_by_name['setLeds'])
_COPROCREQ.fields_by_name['setLeds'].containing_oneof = _COPROCREQ.oneofs_by_name['payload']
_COPROCREQ.oneofs_by_name['payload'].fields.append(
  _COPROCREQ.fields_by_name['getButtons'])
_COPROCREQ.fields_by_name['getButtons'].containing_oneof = _COPROCREQ.oneofs_by_name['payload']
_COPROCSTAT_LEDSSTAT.containing_type = _COPROCSTAT
_COPROCSTAT_BUTTONSSTAT.fields_by_name['buttonsPressed'].enum_type = _COPROCSTAT_BUTTONSENUM
_COPROCSTAT_BUTTONSSTAT.containing_type = _COPROCSTAT
_COPROCSTAT.fields_by_name['ledsStat'].message_type = _COPROCSTAT_LEDSSTAT
_COPROCSTAT.fields_by_name['buttonsStat'].message_type = _COPROCSTAT_BUTTONSSTAT
_COPROCSTAT_BUTTONSENUM.containing_type = _COPROCSTAT
_COPROCSTAT.oneofs_by_name['payload'].fields.append(
  _COPROCSTAT.fields_by_name['ledsStat'])
_COPROCSTAT.fields_by_name['ledsStat'].containing_oneof = _COPROCSTAT.oneofs_by_name['payload']
_COPROCSTAT.oneofs_by_name['payload'].fields.append(
  _COPROCSTAT.fields_by_name['buttonsStat'])
_COPROCSTAT.fields_by_name['buttonsStat'].containing_oneof = _COPROCSTAT.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['CoprocReq'] = _COPROCREQ
DESCRIPTOR.message_types_by_name['CoprocStat'] = _COPROCSTAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CoprocReq = _reflection.GeneratedProtocolMessageType('CoprocReq', (_message.Message,), {

  'SetLeds' : _reflection.GeneratedProtocolMessageType('SetLeds', (_message.Message,), {
    'DESCRIPTOR' : _COPROCREQ_SETLEDS,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocReq.SetLeds)
    })
  ,

  'GetButtons' : _reflection.GeneratedProtocolMessageType('GetButtons', (_message.Message,), {
    'DESCRIPTOR' : _COPROCREQ_GETBUTTONS,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocReq.GetButtons)
    })
  ,
  'DESCRIPTOR' : _COPROCREQ,
  '__module__' : 'rbcx_pb2'
  # @@protoc_insertion_point(class_scope:CoprocReq)
  })
_sym_db.RegisterMessage(CoprocReq)
_sym_db.RegisterMessage(CoprocReq.SetLeds)
_sym_db.RegisterMessage(CoprocReq.GetButtons)

CoprocStat = _reflection.GeneratedProtocolMessageType('CoprocStat', (_message.Message,), {

  'LedsStat' : _reflection.GeneratedProtocolMessageType('LedsStat', (_message.Message,), {
    'DESCRIPTOR' : _COPROCSTAT_LEDSSTAT,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocStat.LedsStat)
    })
  ,

  'ButtonsStat' : _reflection.GeneratedProtocolMessageType('ButtonsStat', (_message.Message,), {
    'DESCRIPTOR' : _COPROCSTAT_BUTTONSSTAT,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocStat.ButtonsStat)
    })
  ,
  'DESCRIPTOR' : _COPROCSTAT,
  '__module__' : 'rbcx_pb2'
  # @@protoc_insertion_point(class_scope:CoprocStat)
  })
_sym_db.RegisterMessage(CoprocStat)
_sym_db.RegisterMessage(CoprocStat.LedsStat)
_sym_db.RegisterMessage(CoprocStat.ButtonsStat)


# @@protoc_insertion_point(module_scope)
