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
  serialized_pb=b'\n\nrbcx.proto\"\x06\n\x04None\"\x8f\x04\n\tCoprocReq\x12\x1a\n\tkeepalive\x18\x01 \x01(\x0b\x32\x05.NoneH\x00\x12%\n\x07setLeds\x18\x04 \x01(\x0b\x32\x12.CoprocReq.SetLedsH\x00\x12+\n\ngetButtons\x18\x05 \x01(\x0b\x32\x15.CoprocReq.GetButtonsH\x00\x12\x33\n\x0esetStupidServo\x18\x06 \x01(\x0b\x32\x19.CoprocReq.SetStupidServoH\x00\x12\x31\n\rultrasoundReq\x18\x07 \x01(\x0b\x32\x18.CoprocReq.UltrasoundReqH\x00\x1a.\n\x07SetLeds\x12#\n\x06ledsOn\x18\x01 \x01(\x0e\x32\x13.CoprocReq.LedsEnum\x1a\x0c\n\nGetButtons\x1a\x61\n\x0eSetStupidServo\x12\x12\n\nservoIndex\x18\x01 \x01(\r\x12\x18\n\x07\x64isable\x18\x04 \x01(\x0b\x32\x05.NoneH\x00\x12\x15\n\x0bsetPosition\x18\x05 \x01(\x02H\x00\x42\n\n\x08servoCmd\x1aH\n\rUltrasoundReq\x12\x10\n\x08utsIndex\x18\x01 \x01(\r\x12\x1b\n\nsinglePing\x18\x04 \x01(\x0b\x32\x05.NoneH\x00\x42\x08\n\x06utsCmd\"4\n\x08LedsEnum\x12\x08\n\x04NONE\x10\x00\x12\x06\n\x02L1\x10\x01\x12\x06\n\x02L2\x10\x02\x12\x06\n\x02L3\x10\x04\x12\x06\n\x02L4\x10\x08\x42\t\n\x07payload\"\x86\x03\n\nCoprocStat\x12\x19\n\x08ledsStat\x18\x04 \x01(\x0b\x32\x05.NoneH\x00\x12.\n\x0b\x62uttonsStat\x18\x05 \x01(\x0b\x32\x17.CoprocStat.ButtonsStatH\x00\x12 \n\x0fstupidServoStat\x18\x06 \x01(\x0b\x32\x05.NoneH\x00\x12\x34\n\x0eultrasoundStat\x18\x07 \x01(\x0b\x32\x1a.CoprocStat.UltrasoundStatH\x00\x1a>\n\x0b\x42uttonsStat\x12/\n\x0e\x62uttonsPressed\x18\x01 \x01(\x0e\x32\x17.CoprocStat.ButtonsEnum\x1a>\n\x0eUltrasoundStat\x12\x10\n\x08utsIndex\x18\x01 \x01(\r\x12\x1a\n\x12roundtripMicrosecs\x18\x02 \x01(\r\"J\n\x0b\x42uttonsEnum\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04\x42OFF\x10\x01\x12\x06\n\x02\x42\x31\x10\x02\x12\x06\n\x02\x42\x32\x10\x04\x12\x06\n\x02\x42\x33\x10\x08\x12\x06\n\x02\x42\x34\x10\x10\x12\x07\n\x03\x42ON\x10 B\t\n\x07payloadb\x06proto3'
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
  serialized_start=487,
  serialized_end=539,
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
  serialized_start=858,
  serialized_end=932,
)
_sym_db.RegisterEnumDescriptor(_COPROCSTAT_BUTTONSENUM)


_NONE = _descriptor.Descriptor(
  name='None',
  full_name='None',
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
  serialized_start=14,
  serialized_end=20,
)


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
  serialized_start=252,
  serialized_end=298,
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
  serialized_start=300,
  serialized_end=312,
)

_COPROCREQ_SETSTUPIDSERVO = _descriptor.Descriptor(
  name='SetStupidServo',
  full_name='CoprocReq.SetStupidServo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servoIndex', full_name='CoprocReq.SetStupidServo.servoIndex', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable', full_name='CoprocReq.SetStupidServo.disable', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setPosition', full_name='CoprocReq.SetStupidServo.setPosition', index=2,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
    _descriptor.OneofDescriptor(
      name='servoCmd', full_name='CoprocReq.SetStupidServo.servoCmd',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=314,
  serialized_end=411,
)

_COPROCREQ_ULTRASOUNDREQ = _descriptor.Descriptor(
  name='UltrasoundReq',
  full_name='CoprocReq.UltrasoundReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='utsIndex', full_name='CoprocReq.UltrasoundReq.utsIndex', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='singlePing', full_name='CoprocReq.UltrasoundReq.singlePing', index=1,
      number=4, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='utsCmd', full_name='CoprocReq.UltrasoundReq.utsCmd',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=413,
  serialized_end=485,
)

_COPROCREQ = _descriptor.Descriptor(
  name='CoprocReq',
  full_name='CoprocReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keepalive', full_name='CoprocReq.keepalive', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setLeds', full_name='CoprocReq.setLeds', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='getButtons', full_name='CoprocReq.getButtons', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setStupidServo', full_name='CoprocReq.setStupidServo', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ultrasoundReq', full_name='CoprocReq.ultrasoundReq', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COPROCREQ_SETLEDS, _COPROCREQ_GETBUTTONS, _COPROCREQ_SETSTUPIDSERVO, _COPROCREQ_ULTRASOUNDREQ, ],
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
  serialized_start=23,
  serialized_end=550,
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
  serialized_start=730,
  serialized_end=792,
)

_COPROCSTAT_ULTRASOUNDSTAT = _descriptor.Descriptor(
  name='UltrasoundStat',
  full_name='CoprocStat.UltrasoundStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='utsIndex', full_name='CoprocStat.UltrasoundStat.utsIndex', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roundtripMicrosecs', full_name='CoprocStat.UltrasoundStat.roundtripMicrosecs', index=1,
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
  serialized_start=794,
  serialized_end=856,
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
    _descriptor.FieldDescriptor(
      name='stupidServoStat', full_name='CoprocStat.stupidServoStat', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ultrasoundStat', full_name='CoprocStat.ultrasoundStat', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COPROCSTAT_BUTTONSSTAT, _COPROCSTAT_ULTRASOUNDSTAT, ],
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
  serialized_start=553,
  serialized_end=943,
)

_COPROCREQ_SETLEDS.fields_by_name['ledsOn'].enum_type = _COPROCREQ_LEDSENUM
_COPROCREQ_SETLEDS.containing_type = _COPROCREQ
_COPROCREQ_GETBUTTONS.containing_type = _COPROCREQ
_COPROCREQ_SETSTUPIDSERVO.fields_by_name['disable'].message_type = _NONE
_COPROCREQ_SETSTUPIDSERVO.containing_type = _COPROCREQ
_COPROCREQ_SETSTUPIDSERVO.oneofs_by_name['servoCmd'].fields.append(
  _COPROCREQ_SETSTUPIDSERVO.fields_by_name['disable'])
_COPROCREQ_SETSTUPIDSERVO.fields_by_name['disable'].containing_oneof = _COPROCREQ_SETSTUPIDSERVO.oneofs_by_name['servoCmd']
_COPROCREQ_SETSTUPIDSERVO.oneofs_by_name['servoCmd'].fields.append(
  _COPROCREQ_SETSTUPIDSERVO.fields_by_name['setPosition'])
_COPROCREQ_SETSTUPIDSERVO.fields_by_name['setPosition'].containing_oneof = _COPROCREQ_SETSTUPIDSERVO.oneofs_by_name['servoCmd']
_COPROCREQ_ULTRASOUNDREQ.fields_by_name['singlePing'].message_type = _NONE
_COPROCREQ_ULTRASOUNDREQ.containing_type = _COPROCREQ
_COPROCREQ_ULTRASOUNDREQ.oneofs_by_name['utsCmd'].fields.append(
  _COPROCREQ_ULTRASOUNDREQ.fields_by_name['singlePing'])
_COPROCREQ_ULTRASOUNDREQ.fields_by_name['singlePing'].containing_oneof = _COPROCREQ_ULTRASOUNDREQ.oneofs_by_name['utsCmd']
_COPROCREQ.fields_by_name['keepalive'].message_type = _NONE
_COPROCREQ.fields_by_name['setLeds'].message_type = _COPROCREQ_SETLEDS
_COPROCREQ.fields_by_name['getButtons'].message_type = _COPROCREQ_GETBUTTONS
_COPROCREQ.fields_by_name['setStupidServo'].message_type = _COPROCREQ_SETSTUPIDSERVO
_COPROCREQ.fields_by_name['ultrasoundReq'].message_type = _COPROCREQ_ULTRASOUNDREQ
_COPROCREQ_LEDSENUM.containing_type = _COPROCREQ
_COPROCREQ.oneofs_by_name['payload'].fields.append(
  _COPROCREQ.fields_by_name['keepalive'])
_COPROCREQ.fields_by_name['keepalive'].containing_oneof = _COPROCREQ.oneofs_by_name['payload']
_COPROCREQ.oneofs_by_name['payload'].fields.append(
  _COPROCREQ.fields_by_name['setLeds'])
_COPROCREQ.fields_by_name['setLeds'].containing_oneof = _COPROCREQ.oneofs_by_name['payload']
_COPROCREQ.oneofs_by_name['payload'].fields.append(
  _COPROCREQ.fields_by_name['getButtons'])
_COPROCREQ.fields_by_name['getButtons'].containing_oneof = _COPROCREQ.oneofs_by_name['payload']
_COPROCREQ.oneofs_by_name['payload'].fields.append(
  _COPROCREQ.fields_by_name['setStupidServo'])
_COPROCREQ.fields_by_name['setStupidServo'].containing_oneof = _COPROCREQ.oneofs_by_name['payload']
_COPROCREQ.oneofs_by_name['payload'].fields.append(
  _COPROCREQ.fields_by_name['ultrasoundReq'])
_COPROCREQ.fields_by_name['ultrasoundReq'].containing_oneof = _COPROCREQ.oneofs_by_name['payload']
_COPROCSTAT_BUTTONSSTAT.fields_by_name['buttonsPressed'].enum_type = _COPROCSTAT_BUTTONSENUM
_COPROCSTAT_BUTTONSSTAT.containing_type = _COPROCSTAT
_COPROCSTAT_ULTRASOUNDSTAT.containing_type = _COPROCSTAT
_COPROCSTAT.fields_by_name['ledsStat'].message_type = _NONE
_COPROCSTAT.fields_by_name['buttonsStat'].message_type = _COPROCSTAT_BUTTONSSTAT
_COPROCSTAT.fields_by_name['stupidServoStat'].message_type = _NONE
_COPROCSTAT.fields_by_name['ultrasoundStat'].message_type = _COPROCSTAT_ULTRASOUNDSTAT
_COPROCSTAT_BUTTONSENUM.containing_type = _COPROCSTAT
_COPROCSTAT.oneofs_by_name['payload'].fields.append(
  _COPROCSTAT.fields_by_name['ledsStat'])
_COPROCSTAT.fields_by_name['ledsStat'].containing_oneof = _COPROCSTAT.oneofs_by_name['payload']
_COPROCSTAT.oneofs_by_name['payload'].fields.append(
  _COPROCSTAT.fields_by_name['buttonsStat'])
_COPROCSTAT.fields_by_name['buttonsStat'].containing_oneof = _COPROCSTAT.oneofs_by_name['payload']
_COPROCSTAT.oneofs_by_name['payload'].fields.append(
  _COPROCSTAT.fields_by_name['stupidServoStat'])
_COPROCSTAT.fields_by_name['stupidServoStat'].containing_oneof = _COPROCSTAT.oneofs_by_name['payload']
_COPROCSTAT.oneofs_by_name['payload'].fields.append(
  _COPROCSTAT.fields_by_name['ultrasoundStat'])
_COPROCSTAT.fields_by_name['ultrasoundStat'].containing_oneof = _COPROCSTAT.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['None'] = _NONE
DESCRIPTOR.message_types_by_name['CoprocReq'] = _COPROCREQ
DESCRIPTOR.message_types_by_name['CoprocStat'] = _COPROCSTAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

globals()['None'] = _reflection.GeneratedProtocolMessageType('None', (_message.Message,), {
  'DESCRIPTOR' : _NONE,
  '__module__' : 'rbcx_pb2'
  # @@protoc_insertion_point(class_scope:None)
  })
_sym_db.RegisterMessage(globals()['None'])

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

  'SetStupidServo' : _reflection.GeneratedProtocolMessageType('SetStupidServo', (_message.Message,), {
    'DESCRIPTOR' : _COPROCREQ_SETSTUPIDSERVO,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocReq.SetStupidServo)
    })
  ,

  'UltrasoundReq' : _reflection.GeneratedProtocolMessageType('UltrasoundReq', (_message.Message,), {
    'DESCRIPTOR' : _COPROCREQ_ULTRASOUNDREQ,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocReq.UltrasoundReq)
    })
  ,
  'DESCRIPTOR' : _COPROCREQ,
  '__module__' : 'rbcx_pb2'
  # @@protoc_insertion_point(class_scope:CoprocReq)
  })
_sym_db.RegisterMessage(CoprocReq)
_sym_db.RegisterMessage(CoprocReq.SetLeds)
_sym_db.RegisterMessage(CoprocReq.GetButtons)
_sym_db.RegisterMessage(CoprocReq.SetStupidServo)
_sym_db.RegisterMessage(CoprocReq.UltrasoundReq)

CoprocStat = _reflection.GeneratedProtocolMessageType('CoprocStat', (_message.Message,), {

  'ButtonsStat' : _reflection.GeneratedProtocolMessageType('ButtonsStat', (_message.Message,), {
    'DESCRIPTOR' : _COPROCSTAT_BUTTONSSTAT,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocStat.ButtonsStat)
    })
  ,

  'UltrasoundStat' : _reflection.GeneratedProtocolMessageType('UltrasoundStat', (_message.Message,), {
    'DESCRIPTOR' : _COPROCSTAT_ULTRASOUNDSTAT,
    '__module__' : 'rbcx_pb2'
    # @@protoc_insertion_point(class_scope:CoprocStat.UltrasoundStat)
    })
  ,
  'DESCRIPTOR' : _COPROCSTAT,
  '__module__' : 'rbcx_pb2'
  # @@protoc_insertion_point(class_scope:CoprocStat)
  })
_sym_db.RegisterMessage(CoprocStat)
_sym_db.RegisterMessage(CoprocStat.ButtonsStat)
_sym_db.RegisterMessage(CoprocStat.UltrasoundStat)


# @@protoc_insertion_point(module_scope)
