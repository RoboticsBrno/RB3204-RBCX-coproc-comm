# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rbcx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nrbcx.proto\x1a\x0cnanopb.proto\"\x06\n\x04None\"+\n\x08RegCoefs\x12\t\n\x01p\x18\x01 \x01(\r\x12\t\n\x01i\x18\x02 \x01(\r\x12\t\n\x01\x64\x18\x03 \x01(\r\"G\n\x0bMotorConfig\x12\x12\n\nvelEpsilon\x18\x01 \x01(\r\x12\x12\n\nposEpsilon\x18\x02 \x01(\r\x12\x10\n\x08maxAccel\x18\x03 \x01(\r\"\xef\x18\n\tCoprocReq\x12\x1a\n\tkeepalive\x18\x01 \x01(\x0b\x32\x05.NoneH\x00\x12%\n\x07setLeds\x18\x04 \x01(\x0b\x32\x12.CoprocReq.SetLedsH\x00\x12+\n\ngetButtons\x18\x05 \x01(\x0b\x32\x15.CoprocReq.GetButtonsH\x00\x12\x33\n\x0esetStupidServo\x18\x06 \x01(\x0b\x32\x19.CoprocReq.SetStupidServoH\x00\x12\x31\n\rultrasoundReq\x18\x07 \x01(\x0b\x32\x18.CoprocReq.UltrasoundReqH\x00\x12\'\n\x08motorReq\x18\x08 \x01(\x0b\x32\x13.CoprocReq.MotorReqH\x00\x12)\n\tbuzzerReq\x18\t \x01(\x0b\x32\x14.CoprocReq.BuzzerReqH\x00\x12\x33\n\x0e\x63\x61libratePower\x18\n \x01(\x0b\x32\x19.CoprocReq.CalibratePowerH\x00\x12\x1e\n\rshutdownPower\x18\x0b \x01(\x0b\x32\x05.NoneH\x00\x12\x1b\n\nversionReq\x18\x0c \x01(\x0b\x32\x05.NoneH\x00\x12#\n\x06rtcReq\x18\r \x01(\x0b\x32\x11.CoprocReq.RtcReqH\x00\x12#\n\x06i2cReq\x18\x0e \x01(\x0b\x32\x11.CoprocReq.I2cReqH\x00\x1a.\n\x07SetLeds\x12#\n\x06ledsOn\x18\x01 \x01(\x0e\x32\x13.CoprocReq.LedsEnum\x1a\x0c\n\nGetButtons\x1a\x61\n\x0eSetStupidServo\x12\x12\n\nservoIndex\x18\x01 \x01(\r\x12\x18\n\x07\x64isable\x18\x04 \x01(\x0b\x32\x05.NoneH\x00\x12\x15\n\x0bsetPosition\x18\x05 \x01(\x02H\x00\x42\n\n\x08servoCmd\x1aH\n\rUltrasoundReq\x12\x10\n\x08utsIndex\x18\x01 \x01(\r\x12\x1b\n\nsinglePing\x18\x04 \x01(\x0b\x32\x05.NoneH\x00\x42\x08\n\x06utsCmd\x1a?\n\x10SetMotorCoupling\x12\x12\n\ncoupleAxis\x18\x01 \x01(\r\x12\x17\n\x0f\x63oupleCoefPower\x18\x02 \x01(\x05\x1a\xf7\x03\n\x08MotorReq\x12\x12\n\nmotorIndex\x18\x01 \x01(\r\x12\x19\n\x08getState\x18\x04 \x01(\x0b\x32\x05.NoneH\x00\x12\x12\n\x08setPower\x18\x05 \x01(\x11H\x00\x12\x12\n\x08setBrake\x18\x06 \x01(\x11H\x00\x12\x15\n\x0bsetVelocity\x18\x07 \x01(\x11H\x00\x12\x16\n\x0chomePosition\x18\x08 \x01(\x11H\x00\x12\x36\n\x0bsetPosition\x18\n \x01(\x0b\x32\x1f.CoprocReq.MotorReq.SetPositionH\x00\x12\x36\n\x0b\x61\x64\x64Position\x18\x0b \x01(\x0b\x32\x1f.CoprocReq.MotorReq.SetPositionH\x00\x12(\n\x13setVelocityRegCoefs\x18\x10 \x01(\x0b\x32\t.RegCoefsH\x00\x12(\n\x13setPositionRegCoefs\x18\x11 \x01(\x0b\x32\t.RegCoefsH\x00\x12!\n\tsetConfig\x18\x12 \x01(\x0b\x32\x0c.MotorConfigH\x00\x12\x32\n\x0bsetCoupling\x18\x13 \x01(\x0b\x32\x1b.CoprocReq.SetMotorCouplingH\x00\x1a>\n\x0bSetPosition\x12\x16\n\x0etargetPosition\x18\x01 \x01(\x11\x12\x17\n\x0frunningVelocity\x18\x02 \x01(\x11\x42\n\n\x08motorCmd\x1a\x17\n\tBuzzerReq\x12\n\n\x02on\x18\x01 \x01(\x08\x1aZ\n\x0e\x43\x61libratePower\x12\r\n\x05vccMv\x18\x01 \x01(\r\x12\x11\n\tbattMidMv\x18\x02 \x01(\r\x12\x10\n\x08vRef33Mv\x18\x03 \x01(\r\x12\x14\n\x0ctemperatureC\x18\x04 \x01(\r\x1aO\n\x06RtcReq\x12\x14\n\x03get\x18\x01 \x01(\x0b\x32\x05.NoneH\x00\x12\x11\n\x07setTime\x18\x02 \x01(\rH\x00\x12\x12\n\x08setAlarm\x18\x03 \x01(\rH\x00\x42\x08\n\x06rtcCmd\x1a_\n\x06I2cReq\x12%\n\x07oledReq\x18\x01 \x01(\x0b\x32\x12.CoprocReq.OledReqH\x00\x12#\n\x06mpuReq\x18\x02 \x01(\x0b\x32\x11.CoprocReq.MpuReqH\x00\x42\t\n\x07payload\x1a\xc9\x03\n\x07OledReq\x12#\n\x04init\x18\x01 \x01(\x0b\x32\x13.CoprocReq.OledInitH\x00\x12$\n\x04\x66ill\x18\x02 \x01(\x0e\x32\x14.CoprocReq.OledColorH\x00\x12\x17\n\x06update\x18\x03 \x01(\x0b\x32\x05.NoneH\x00\x12-\n\tdrawPixel\x18\x04 \x01(\x0b\x32\x18.CoprocReq.OledDrawPixelH\x00\x12\x31\n\x0bwriteString\x18\x05 \x01(\x0b\x32\x1a.CoprocReq.OledWriteStringH\x00\x12-\n\tsetCursor\x18\x06 \x01(\x0b\x32\x18.CoprocReq.OledSetCursorH\x00\x12+\n\x08\x64rawLine\x18\x07 \x01(\x0b\x32\x17.CoprocReq.OledDrawLineH\x00\x12)\n\x07\x64rawArc\x18\x08 \x01(\x0b\x32\x16.CoprocReq.OledDrawArcH\x00\x12/\n\ndrawCircle\x18\t \x01(\x0b\x32\x19.CoprocReq.OledDrawCircleH\x00\x12\x35\n\rdrawRectangle\x18\n \x01(\x0b\x32\x1c.CoprocReq.OledDrawRectangleH\x00\x42\t\n\x07oledCmd\x1aO\n\x08OledInit\x12\x0e\n\x06height\x18\x01 \x01(\r\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06rotate\x18\x03 \x01(\x08\x12\x14\n\x0cinverseColor\x18\x04 \x01(\x08\x1aJ\n\rOledDrawPixel\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x12#\n\x05\x63olor\x18\x03 \x01(\x0e\x32\x14.CoprocReq.OledColor\x1an\n\x0fOledWriteString\x12\x13\n\x04text\x18\x01 \x01(\tB\x05\x92?\x02p \x12!\n\x04\x66ont\x18\x02 \x01(\x0e\x32\x13.CoprocReq.OledFont\x12#\n\x05\x63olor\x18\x03 \x01(\x0e\x32\x14.CoprocReq.OledColor\x1a%\n\rOledSetCursor\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x1a\x63\n\x0cOledDrawLine\x12\n\n\x02x1\x18\x01 \x01(\r\x12\n\n\x02y1\x18\x02 \x01(\r\x12\n\n\x02x2\x18\x03 \x01(\r\x12\n\n\x02y2\x18\x04 \x01(\r\x12#\n\x05\x63olor\x18\x05 \x01(\x0e\x32\x14.CoprocReq.OledColor\x1a|\n\x0bOledDrawArc\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x12\x0e\n\x06radius\x18\x03 \x01(\r\x12\x13\n\x0bstart_angle\x18\x04 \x01(\r\x12\r\n\x05sweep\x18\x05 \x01(\r\x12#\n\x05\x63olor\x18\x06 \x01(\x0e\x32\x14.CoprocReq.OledColor\x1a[\n\x0eOledDrawCircle\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x12\x0e\n\x06radius\x18\x03 \x01(\r\x12#\n\x05\x63olor\x18\x04 \x01(\x0e\x32\x14.CoprocReq.OledColor\x1ah\n\x11OledDrawRectangle\x12\n\n\x02x1\x18\x01 \x01(\r\x12\n\n\x02y1\x18\x02 \x01(\r\x12\n\n\x02x2\x18\x03 \x01(\r\x12\n\n\x02y2\x18\x04 \x01(\r\x12#\n\x05\x63olor\x18\x05 \x01(\x0e\x32\x14.CoprocReq.OledColor\x1a\xb7\x01\n\x06MpuReq\x12\x15\n\x04init\x18\x01 \x01(\x0b\x32\x05.NoneH\x00\x12\x18\n\x07oneSend\x18\x02 \x01(\x0b\x32\x05.NoneH\x00\x12\x1a\n\tstartSend\x18\x03 \x01(\x0b\x32\x05.NoneH\x00\x12\x19\n\x08stopSend\x18\x04 \x01(\x0b\x32\x05.NoneH\x00\x12\x19\n\x0fsetCompressCoef\x18\x05 \x01(\rH\x00\x12 \n\x0fgetCompressCoef\x18\x06 \x01(\x0b\x32\x05.NoneH\x00\x42\x08\n\x06mpuCmd\"4\n\x08LedsEnum\x12\x08\n\x04NONE\x10\x00\x12\x06\n\x02L1\x10\x01\x12\x06\n\x02L2\x10\x02\x12\x06\n\x02L3\x10\x04\x12\x06\n\x02L4\x10\x08\"+\n\tOledColor\x12\x0e\n\nOLED_BLACK\x10\x00\x12\x0e\n\nOLED_WHITE\x10\x01\"[\n\x08OledFont\x12\x11\n\rOLED_FONT_6X8\x10\x00\x12\x12\n\x0eOLED_FONT_7X10\x10\x01\x12\x13\n\x0fOLED_FONT_11X18\x10\x02\x12\x13\n\x0fOLED_FONT_16X26\x10\x03\x42\t\n\x07payload\"\x83\n\n\nCoprocStat\x12\x19\n\x08ledsStat\x18\x04 \x01(\x0b\x32\x05.NoneH\x00\x12.\n\x0b\x62uttonsStat\x18\x05 \x01(\x0b\x32\x17.CoprocStat.ButtonsStatH\x00\x12 \n\x0fstupidServoStat\x18\x06 \x01(\x0b\x32\x05.NoneH\x00\x12\x34\n\x0eultrasoundStat\x18\x07 \x01(\x0b\x32\x1a.CoprocStat.UltrasoundStatH\x00\x12\x30\n\x0cpowerAdcStat\x18\x08 \x01(\x0b\x32\x18.CoprocStat.PowerAdcStatH\x00\x12.\n\x0bversionStat\x18\t \x01(\x0b\x32\x17.CoprocStat.VersionStatH\x00\x12*\n\tmotorStat\x18\n \x01(\x0b\x32\x15.CoprocStat.MotorStatH\x00\x12&\n\x07rtcStat\x18\x0b \x01(\x0b\x32\x13.CoprocStat.RtcStatH\x00\x12*\n\tfaultStat\x18\x0c \x01(\x0b\x32\x15.CoprocStat.FaultStatH\x00\x12&\n\x07mpuStat\x18\r \x01(\x0b\x32\x13.CoprocStat.MpuStatH\x00\x1a>\n\x0b\x42uttonsStat\x12/\n\x0e\x62uttonsPressed\x18\x01 \x01(\x0e\x32\x17.CoprocStat.ButtonsEnum\x1a>\n\x0eUltrasoundStat\x12\x10\n\x08utsIndex\x18\x01 \x01(\r\x12\x1a\n\x12roundtripMicrosecs\x18\x02 \x01(\r\x1al\n\tMotorStat\x12\x12\n\nmotorIndex\x18\x01 \x01(\r\x12\x18\n\x04mode\x18\x02 \x01(\x0e\x32\n.MotorMode\x12\r\n\x05power\x18\x03 \x01(\x11\x12\x10\n\x08velocity\x18\x04 \x01(\x11\x12\x10\n\x08position\x18\x05 \x01(\x11\x1a\x46\n\x0cPowerAdcStat\x12\r\n\x05vccMv\x18\x01 \x01(\r\x12\x11\n\tbattMidMv\x18\x02 \x01(\r\x12\x14\n\x0ctemperatureC\x18\x03 \x01(\x05\x1aJ\n\x0bVersionStat\x12\x1c\n\x08revision\x18\x01 \x01(\x0c\x42\n\x92?\x02\x08\x08\x92?\x02x\x01\x12\x0e\n\x06number\x18\x02 \x01(\r\x12\r\n\x05\x64irty\x18\x03 \x01(\x08\x1aK\n\x07RtcStat\x12\x0c\n\x04time\x18\x01 \x01(\r\x12\r\n\x05\x61larm\x18\x02 \x01(\r\x12#\n\x05\x66lags\x18\x03 \x01(\x0e\x32\x14.CoprocStat.RtcFlags\x1aK\n\tFaultStat\x12\x1a\n\toledFault\x18\x01 \x01(\x0b\x32\x05.NoneH\x00\x12\x19\n\x08mpuFault\x18\x02 \x01(\x0b\x32\x05.NoneH\x00\x42\x07\n\x05\x66\x61ult\x1aj\n\x07MpuStat\x12\x14\n\x0c\x63ompressCoef\x18\x01 \x01(\r\x12$\n\x05\x61\x63\x63\x65l\x18\x02 \x01(\x0b\x32\x15.CoprocStat.MpuVector\x12#\n\x04gyro\x18\x03 \x01(\x0b\x32\x15.CoprocStat.MpuVector\x1a,\n\tMpuVector\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\t\n\x01z\x18\x03 \x01(\x05\"K\n\x0b\x42uttonsEnum\x12\t\n\x05\x42NONE\x10\x00\x12\x08\n\x04\x42OFF\x10\x01\x12\x06\n\x02\x42\x31\x10\x02\x12\x06\n\x02\x42\x32\x10\x04\x12\x06\n\x02\x42\x33\x10\x08\x12\x06\n\x02\x42\x34\x10\x10\x12\x07\n\x03\x42ON\x10 \":\n\x08RtcFlags\x12\x0c\n\x08RTC_NONE\x10\x00\x12\x11\n\rRTC_NOT_READY\x10\x01\x12\r\n\tRTC_ALARM\x10\x02\x42\t\n\x07payload*b\n\tMotorMode\x12\t\n\x05POWER\x10\x00\x12\t\n\x05\x42RAKE\x10\x01\x12\x0c\n\x08VELOCITY\x10\x02\x12\x0c\n\x08POSITION\x10\x03\x12\x11\n\rPOSITION_IDLE\x10\x04\x12\x10\n\x0c\x43OUPLE_POWER\x10\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rbcx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COPROCREQ_OLEDWRITESTRING.fields_by_name['text']._options = None
  _COPROCREQ_OLEDWRITESTRING.fields_by_name['text']._serialized_options = b'\222?\002p '
  _COPROCSTAT_VERSIONSTAT.fields_by_name['revision']._options = None
  _COPROCSTAT_VERSIONSTAT.fields_by_name['revision']._serialized_options = b'\222?\002\010\010\222?\002x\001'
  _MOTORMODE._serialized_start=4626
  _MOTORMODE._serialized_end=4724
  _NONE._serialized_start=28
  _NONE._serialized_end=34
  _REGCOEFS._serialized_start=36
  _REGCOEFS._serialized_end=79
  _MOTORCONFIG._serialized_start=81
  _MOTORCONFIG._serialized_end=152
  _COPROCREQ._serialized_start=155
  _COPROCREQ._serialized_end=3338
  _COPROCREQ_SETLEDS._serialized_start=656
  _COPROCREQ_SETLEDS._serialized_end=702
  _COPROCREQ_GETBUTTONS._serialized_start=704
  _COPROCREQ_GETBUTTONS._serialized_end=716
  _COPROCREQ_SETSTUPIDSERVO._serialized_start=718
  _COPROCREQ_SETSTUPIDSERVO._serialized_end=815
  _COPROCREQ_ULTRASOUNDREQ._serialized_start=817
  _COPROCREQ_ULTRASOUNDREQ._serialized_end=889
  _COPROCREQ_SETMOTORCOUPLING._serialized_start=891
  _COPROCREQ_SETMOTORCOUPLING._serialized_end=954
  _COPROCREQ_MOTORREQ._serialized_start=957
  _COPROCREQ_MOTORREQ._serialized_end=1460
  _COPROCREQ_MOTORREQ_SETPOSITION._serialized_start=1386
  _COPROCREQ_MOTORREQ_SETPOSITION._serialized_end=1448
  _COPROCREQ_BUZZERREQ._serialized_start=1462
  _COPROCREQ_BUZZERREQ._serialized_end=1485
  _COPROCREQ_CALIBRATEPOWER._serialized_start=1487
  _COPROCREQ_CALIBRATEPOWER._serialized_end=1577
  _COPROCREQ_RTCREQ._serialized_start=1579
  _COPROCREQ_RTCREQ._serialized_end=1658
  _COPROCREQ_I2CREQ._serialized_start=1660
  _COPROCREQ_I2CREQ._serialized_end=1755
  _COPROCREQ_OLEDREQ._serialized_start=1758
  _COPROCREQ_OLEDREQ._serialized_end=2215
  _COPROCREQ_OLEDINIT._serialized_start=2217
  _COPROCREQ_OLEDINIT._serialized_end=2296
  _COPROCREQ_OLEDDRAWPIXEL._serialized_start=2298
  _COPROCREQ_OLEDDRAWPIXEL._serialized_end=2372
  _COPROCREQ_OLEDWRITESTRING._serialized_start=2374
  _COPROCREQ_OLEDWRITESTRING._serialized_end=2484
  _COPROCREQ_OLEDSETCURSOR._serialized_start=2486
  _COPROCREQ_OLEDSETCURSOR._serialized_end=2523
  _COPROCREQ_OLEDDRAWLINE._serialized_start=2525
  _COPROCREQ_OLEDDRAWLINE._serialized_end=2624
  _COPROCREQ_OLEDDRAWARC._serialized_start=2626
  _COPROCREQ_OLEDDRAWARC._serialized_end=2750
  _COPROCREQ_OLEDDRAWCIRCLE._serialized_start=2752
  _COPROCREQ_OLEDDRAWCIRCLE._serialized_end=2843
  _COPROCREQ_OLEDDRAWRECTANGLE._serialized_start=2845
  _COPROCREQ_OLEDDRAWRECTANGLE._serialized_end=2949
  _COPROCREQ_MPUREQ._serialized_start=2952
  _COPROCREQ_MPUREQ._serialized_end=3135
  _COPROCREQ_LEDSENUM._serialized_start=3137
  _COPROCREQ_LEDSENUM._serialized_end=3189
  _COPROCREQ_OLEDCOLOR._serialized_start=3191
  _COPROCREQ_OLEDCOLOR._serialized_end=3234
  _COPROCREQ_OLEDFONT._serialized_start=3236
  _COPROCREQ_OLEDFONT._serialized_end=3327
  _COPROCSTAT._serialized_start=3341
  _COPROCSTAT._serialized_end=4624
  _COPROCSTAT_BUTTONSSTAT._serialized_start=3784
  _COPROCSTAT_BUTTONSSTAT._serialized_end=3846
  _COPROCSTAT_ULTRASOUNDSTAT._serialized_start=3848
  _COPROCSTAT_ULTRASOUNDSTAT._serialized_end=3910
  _COPROCSTAT_MOTORSTAT._serialized_start=3912
  _COPROCSTAT_MOTORSTAT._serialized_end=4020
  _COPROCSTAT_POWERADCSTAT._serialized_start=4022
  _COPROCSTAT_POWERADCSTAT._serialized_end=4092
  _COPROCSTAT_VERSIONSTAT._serialized_start=4094
  _COPROCSTAT_VERSIONSTAT._serialized_end=4168
  _COPROCSTAT_RTCSTAT._serialized_start=4170
  _COPROCSTAT_RTCSTAT._serialized_end=4245
  _COPROCSTAT_FAULTSTAT._serialized_start=4247
  _COPROCSTAT_FAULTSTAT._serialized_end=4322
  _COPROCSTAT_MPUSTAT._serialized_start=4324
  _COPROCSTAT_MPUSTAT._serialized_end=4430
  _COPROCSTAT_MPUVECTOR._serialized_start=4432
  _COPROCSTAT_MPUVECTOR._serialized_end=4476
  _COPROCSTAT_BUTTONSENUM._serialized_start=4478
  _COPROCSTAT_BUTTONSENUM._serialized_end=4553
  _COPROCSTAT_RTCFLAGS._serialized_start=4555
  _COPROCSTAT_RTCFLAGS._serialized_end=4613
# @@protoc_insertion_point(module_scope)
