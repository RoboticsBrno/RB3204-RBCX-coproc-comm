/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.1 */

#ifndef PB_RBCX_PB_H_INCLUDED
#define PB_RBCX_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _MotorMode {
    MotorMode_POWER = 0,
    MotorMode_BRAKE = 1,
    MotorMode_VELOCITY = 2,
    MotorMode_POSITION = 3
} MotorMode;

typedef enum _CoprocReq_LedsEnum {
    CoprocReq_LedsEnum_NONE = 0,
    CoprocReq_LedsEnum_L1 = 1,
    CoprocReq_LedsEnum_L2 = 2,
    CoprocReq_LedsEnum_L3 = 4,
    CoprocReq_LedsEnum_L4 = 8
} CoprocReq_LedsEnum;

typedef enum _CoprocStat_ButtonsEnum {
    CoprocStat_ButtonsEnum_NONE = 0,
    CoprocStat_ButtonsEnum_BOFF = 1,
    CoprocStat_ButtonsEnum_B1 = 2,
    CoprocStat_ButtonsEnum_B2 = 4,
    CoprocStat_ButtonsEnum_B3 = 8,
    CoprocStat_ButtonsEnum_B4 = 16,
    CoprocStat_ButtonsEnum_BON = 32
} CoprocStat_ButtonsEnum;

/* Struct definitions */
typedef struct _CoprocReq_GetButtons {
    char dummy_field;
} CoprocReq_GetButtons;

typedef struct _None {
    char dummy_field;
} None;

typedef struct _CoprocReq_BuzzerReq {
    bool on;
} CoprocReq_BuzzerReq;

typedef struct _CoprocReq_CalibratePower {
    uint32_t vccMv;
    uint32_t battMidMv;
    uint32_t vRef33Mv;
    uint32_t temperatureC;
} CoprocReq_CalibratePower;

typedef struct _CoprocReq_SetLeds {
    CoprocReq_LedsEnum ledsOn;
} CoprocReq_SetLeds;

typedef struct _CoprocReq_SetStupidServo {
    uint32_t servoIndex;
    pb_size_t which_servoCmd;
    union {
        None disable;
        float setPosition;
    } servoCmd;
} CoprocReq_SetStupidServo;

typedef struct _CoprocReq_UltrasoundReq {
    uint32_t utsIndex;
    pb_size_t which_utsCmd;
    union {
        None singlePing;
    } utsCmd;
} CoprocReq_UltrasoundReq;

typedef struct _CoprocStat_ButtonsStat {
    CoprocStat_ButtonsEnum buttonsPressed;
} CoprocStat_ButtonsStat;

typedef struct _CoprocStat_MotorStat {
    uint32_t motorIndex;
    MotorMode mode;
    int32_t power;
    int32_t velocity;
    int32_t position;
} CoprocStat_MotorStat;

typedef struct _CoprocStat_PowerAdcStat {
    uint32_t vccMv;
    uint32_t battMidMv;
    int32_t temperatureC;
} CoprocStat_PowerAdcStat;

typedef struct _CoprocStat_UltrasoundStat {
    uint32_t utsIndex;
    uint32_t roundtripMicrosecs;
} CoprocStat_UltrasoundStat;

typedef struct _CoprocStat_VersionStat {
    pb_byte_t revision[8];
    uint32_t number;
    bool dirty;
} CoprocStat_VersionStat;

typedef struct _RegCoefs {
    uint32_t p;
    uint32_t i;
    uint32_t d;
} RegCoefs;

typedef struct _CoprocReq_MotorReq {
    uint32_t motorIndex;
    pb_size_t which_motorCmd;
    union {
        None getState;
        int32_t setPower;
        int32_t setBrake;
        int32_t setVelocity;
        int32_t homePosition;
        int32_t setPosition;
        int32_t addPosition;
        RegCoefs setVelocityRegCoefs;
        RegCoefs setPositionRegCoefs;
    } motorCmd;
} CoprocReq_MotorReq;

typedef struct _CoprocStat {
    pb_size_t which_payload;
    union {
        None ledsStat;
        CoprocStat_ButtonsStat buttonsStat;
        None stupidServoStat;
        CoprocStat_UltrasoundStat ultrasoundStat;
        CoprocStat_PowerAdcStat powerAdcStat;
        CoprocStat_VersionStat versionStat;
    } payload;
} CoprocStat;

typedef struct _CoprocReq {
    pb_size_t which_payload;
    union {
        None keepalive;
        CoprocReq_SetLeds setLeds;
        CoprocReq_GetButtons getButtons;
        CoprocReq_SetStupidServo setStupidServo;
        CoprocReq_UltrasoundReq ultrasoundReq;
        CoprocReq_MotorReq motorReq;
        CoprocReq_BuzzerReq buzzerReq;
        CoprocReq_CalibratePower calibratePower;
        None shutdownPower;
        None versionReq;
    } payload;
} CoprocReq;


/* Helper constants for enums */
#define _MotorMode_MIN MotorMode_POWER
#define _MotorMode_MAX MotorMode_POSITION
#define _MotorMode_ARRAYSIZE ((MotorMode)(MotorMode_POSITION+1))

#define _CoprocReq_LedsEnum_MIN CoprocReq_LedsEnum_NONE
#define _CoprocReq_LedsEnum_MAX CoprocReq_LedsEnum_L4
#define _CoprocReq_LedsEnum_ARRAYSIZE ((CoprocReq_LedsEnum)(CoprocReq_LedsEnum_L4+1))

#define _CoprocStat_ButtonsEnum_MIN CoprocStat_ButtonsEnum_NONE
#define _CoprocStat_ButtonsEnum_MAX CoprocStat_ButtonsEnum_BON
#define _CoprocStat_ButtonsEnum_ARRAYSIZE ((CoprocStat_ButtonsEnum)(CoprocStat_ButtonsEnum_BON+1))


/* Initializer values for message structs */
#define None_init_default                        {0}
#define RegCoefs_init_default                    {0, 0, 0}
#define CoprocReq_init_default                   {0, {None_init_default}}
#define CoprocReq_SetLeds_init_default           {_CoprocReq_LedsEnum_MIN}
#define CoprocReq_GetButtons_init_default        {0}
#define CoprocReq_SetStupidServo_init_default    {0, 0, {None_init_default}}
#define CoprocReq_UltrasoundReq_init_default     {0, 0, {None_init_default}}
#define CoprocReq_MotorReq_init_default          {0, 0, {None_init_default}}
#define CoprocReq_BuzzerReq_init_default         {0}
#define CoprocReq_CalibratePower_init_default    {0, 0, 0, 0}
#define CoprocStat_init_default                  {0, {None_init_default}}
#define CoprocStat_ButtonsStat_init_default      {_CoprocStat_ButtonsEnum_MIN}
#define CoprocStat_UltrasoundStat_init_default   {0, 0}
#define CoprocStat_MotorStat_init_default        {0, _MotorMode_MIN, 0, 0, 0}
#define CoprocStat_PowerAdcStat_init_default     {0, 0, 0}
#define CoprocStat_VersionStat_init_default      {{0}, 0, 0}
#define None_init_zero                           {0}
#define RegCoefs_init_zero                       {0, 0, 0}
#define CoprocReq_init_zero                      {0, {None_init_zero}}
#define CoprocReq_SetLeds_init_zero              {_CoprocReq_LedsEnum_MIN}
#define CoprocReq_GetButtons_init_zero           {0}
#define CoprocReq_SetStupidServo_init_zero       {0, 0, {None_init_zero}}
#define CoprocReq_UltrasoundReq_init_zero        {0, 0, {None_init_zero}}
#define CoprocReq_MotorReq_init_zero             {0, 0, {None_init_zero}}
#define CoprocReq_BuzzerReq_init_zero            {0}
#define CoprocReq_CalibratePower_init_zero       {0, 0, 0, 0}
#define CoprocStat_init_zero                     {0, {None_init_zero}}
#define CoprocStat_ButtonsStat_init_zero         {_CoprocStat_ButtonsEnum_MIN}
#define CoprocStat_UltrasoundStat_init_zero      {0, 0}
#define CoprocStat_MotorStat_init_zero           {0, _MotorMode_MIN, 0, 0, 0}
#define CoprocStat_PowerAdcStat_init_zero        {0, 0, 0}
#define CoprocStat_VersionStat_init_zero         {{0}, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define CoprocReq_BuzzerReq_on_tag               1
#define CoprocReq_CalibratePower_vccMv_tag       1
#define CoprocReq_CalibratePower_battMidMv_tag   2
#define CoprocReq_CalibratePower_vRef33Mv_tag    3
#define CoprocReq_CalibratePower_temperatureC_tag 4
#define CoprocReq_SetLeds_ledsOn_tag             1
#define CoprocReq_SetStupidServo_disable_tag     4
#define CoprocReq_SetStupidServo_setPosition_tag 5
#define CoprocReq_SetStupidServo_servoIndex_tag  1
#define CoprocReq_UltrasoundReq_singlePing_tag   4
#define CoprocReq_UltrasoundReq_utsIndex_tag     1
#define CoprocStat_ButtonsStat_buttonsPressed_tag 1
#define CoprocStat_MotorStat_motorIndex_tag      1
#define CoprocStat_MotorStat_mode_tag            2
#define CoprocStat_MotorStat_power_tag           3
#define CoprocStat_MotorStat_velocity_tag        4
#define CoprocStat_MotorStat_position_tag        5
#define CoprocStat_PowerAdcStat_vccMv_tag        1
#define CoprocStat_PowerAdcStat_battMidMv_tag    2
#define CoprocStat_PowerAdcStat_temperatureC_tag 3
#define CoprocStat_UltrasoundStat_utsIndex_tag   1
#define CoprocStat_UltrasoundStat_roundtripMicrosecs_tag 2
#define CoprocStat_VersionStat_revision_tag      1
#define CoprocStat_VersionStat_number_tag        2
#define CoprocStat_VersionStat_dirty_tag         3
#define RegCoefs_p_tag                           1
#define RegCoefs_i_tag                           2
#define RegCoefs_d_tag                           3
#define CoprocReq_MotorReq_getState_tag          4
#define CoprocReq_MotorReq_setPower_tag          5
#define CoprocReq_MotorReq_setBrake_tag          6
#define CoprocReq_MotorReq_setVelocity_tag       7
#define CoprocReq_MotorReq_homePosition_tag      8
#define CoprocReq_MotorReq_setPosition_tag       10
#define CoprocReq_MotorReq_addPosition_tag       11
#define CoprocReq_MotorReq_setVelocityRegCoefs_tag 16
#define CoprocReq_MotorReq_setPositionRegCoefs_tag 17
#define CoprocReq_MotorReq_motorIndex_tag        1
#define CoprocStat_ledsStat_tag                  4
#define CoprocStat_buttonsStat_tag               5
#define CoprocStat_stupidServoStat_tag           6
#define CoprocStat_ultrasoundStat_tag            7
#define CoprocStat_powerAdcStat_tag              8
#define CoprocStat_versionStat_tag               9
#define CoprocReq_keepalive_tag                  1
#define CoprocReq_setLeds_tag                    4
#define CoprocReq_getButtons_tag                 5
#define CoprocReq_setStupidServo_tag             6
#define CoprocReq_ultrasoundReq_tag              7
#define CoprocReq_motorReq_tag                   8
#define CoprocReq_buzzerReq_tag                  9
#define CoprocReq_calibratePower_tag             10
#define CoprocReq_shutdownPower_tag              11
#define CoprocReq_versionReq_tag                 12

/* Struct field encoding specification for nanopb */
#define None_FIELDLIST(X, a) \

#define None_CALLBACK NULL
#define None_DEFAULT NULL

#define RegCoefs_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   p,                 1) \
X(a, STATIC,   SINGULAR, UINT32,   i,                 2) \
X(a, STATIC,   SINGULAR, UINT32,   d,                 3)
#define RegCoefs_CALLBACK NULL
#define RegCoefs_DEFAULT NULL

#define CoprocReq_FIELDLIST(X, a) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,keepalive,payload.keepalive),   1) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,setLeds,payload.setLeds),   4) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,getButtons,payload.getButtons),   5) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,setStupidServo,payload.setStupidServo),   6) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,ultrasoundReq,payload.ultrasoundReq),   7) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,motorReq,payload.motorReq),   8) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,buzzerReq,payload.buzzerReq),   9) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,calibratePower,payload.calibratePower),  10) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,shutdownPower,payload.shutdownPower),  11) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,versionReq,payload.versionReq),  12)
#define CoprocReq_CALLBACK NULL
#define CoprocReq_DEFAULT NULL
#define CoprocReq_payload_keepalive_MSGTYPE None
#define CoprocReq_payload_setLeds_MSGTYPE CoprocReq_SetLeds
#define CoprocReq_payload_getButtons_MSGTYPE CoprocReq_GetButtons
#define CoprocReq_payload_setStupidServo_MSGTYPE CoprocReq_SetStupidServo
#define CoprocReq_payload_ultrasoundReq_MSGTYPE CoprocReq_UltrasoundReq
#define CoprocReq_payload_motorReq_MSGTYPE CoprocReq_MotorReq
#define CoprocReq_payload_buzzerReq_MSGTYPE CoprocReq_BuzzerReq
#define CoprocReq_payload_calibratePower_MSGTYPE CoprocReq_CalibratePower
#define CoprocReq_payload_shutdownPower_MSGTYPE None
#define CoprocReq_payload_versionReq_MSGTYPE None

#define CoprocReq_SetLeds_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UENUM,    ledsOn,            1)
#define CoprocReq_SetLeds_CALLBACK NULL
#define CoprocReq_SetLeds_DEFAULT NULL

#define CoprocReq_GetButtons_FIELDLIST(X, a) \

#define CoprocReq_GetButtons_CALLBACK NULL
#define CoprocReq_GetButtons_DEFAULT NULL

#define CoprocReq_SetStupidServo_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   servoIndex,        1) \
X(a, STATIC,   ONEOF,    MESSAGE,  (servoCmd,disable,servoCmd.disable),   4) \
X(a, STATIC,   ONEOF,    FLOAT,    (servoCmd,setPosition,servoCmd.setPosition),   5)
#define CoprocReq_SetStupidServo_CALLBACK NULL
#define CoprocReq_SetStupidServo_DEFAULT NULL
#define CoprocReq_SetStupidServo_servoCmd_disable_MSGTYPE None

#define CoprocReq_UltrasoundReq_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   utsIndex,          1) \
X(a, STATIC,   ONEOF,    MESSAGE,  (utsCmd,singlePing,utsCmd.singlePing),   4)
#define CoprocReq_UltrasoundReq_CALLBACK NULL
#define CoprocReq_UltrasoundReq_DEFAULT NULL
#define CoprocReq_UltrasoundReq_utsCmd_singlePing_MSGTYPE None

#define CoprocReq_MotorReq_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   motorIndex,        1) \
X(a, STATIC,   ONEOF,    MESSAGE,  (motorCmd,getState,motorCmd.getState),   4) \
X(a, STATIC,   ONEOF,    SINT32,   (motorCmd,setPower,motorCmd.setPower),   5) \
X(a, STATIC,   ONEOF,    SINT32,   (motorCmd,setBrake,motorCmd.setBrake),   6) \
X(a, STATIC,   ONEOF,    SINT32,   (motorCmd,setVelocity,motorCmd.setVelocity),   7) \
X(a, STATIC,   ONEOF,    SINT32,   (motorCmd,homePosition,motorCmd.homePosition),   8) \
X(a, STATIC,   ONEOF,    SINT32,   (motorCmd,setPosition,motorCmd.setPosition),  10) \
X(a, STATIC,   ONEOF,    SINT32,   (motorCmd,addPosition,motorCmd.addPosition),  11) \
X(a, STATIC,   ONEOF,    MESSAGE,  (motorCmd,setVelocityRegCoefs,motorCmd.setVelocityRegCoefs),  16) \
X(a, STATIC,   ONEOF,    MESSAGE,  (motorCmd,setPositionRegCoefs,motorCmd.setPositionRegCoefs),  17)
#define CoprocReq_MotorReq_CALLBACK NULL
#define CoprocReq_MotorReq_DEFAULT NULL
#define CoprocReq_MotorReq_motorCmd_getState_MSGTYPE None
#define CoprocReq_MotorReq_motorCmd_setVelocityRegCoefs_MSGTYPE RegCoefs
#define CoprocReq_MotorReq_motorCmd_setPositionRegCoefs_MSGTYPE RegCoefs

#define CoprocReq_BuzzerReq_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, BOOL,     on,                1)
#define CoprocReq_BuzzerReq_CALLBACK NULL
#define CoprocReq_BuzzerReq_DEFAULT NULL

#define CoprocReq_CalibratePower_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   vccMv,             1) \
X(a, STATIC,   SINGULAR, UINT32,   battMidMv,         2) \
X(a, STATIC,   SINGULAR, UINT32,   vRef33Mv,          3) \
X(a, STATIC,   SINGULAR, UINT32,   temperatureC,      4)
#define CoprocReq_CalibratePower_CALLBACK NULL
#define CoprocReq_CalibratePower_DEFAULT NULL

#define CoprocStat_FIELDLIST(X, a) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,ledsStat,payload.ledsStat),   4) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,buttonsStat,payload.buttonsStat),   5) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,stupidServoStat,payload.stupidServoStat),   6) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,ultrasoundStat,payload.ultrasoundStat),   7) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,powerAdcStat,payload.powerAdcStat),   8) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,versionStat,payload.versionStat),   9)
#define CoprocStat_CALLBACK NULL
#define CoprocStat_DEFAULT NULL
#define CoprocStat_payload_ledsStat_MSGTYPE None
#define CoprocStat_payload_buttonsStat_MSGTYPE CoprocStat_ButtonsStat
#define CoprocStat_payload_stupidServoStat_MSGTYPE None
#define CoprocStat_payload_ultrasoundStat_MSGTYPE CoprocStat_UltrasoundStat
#define CoprocStat_payload_powerAdcStat_MSGTYPE CoprocStat_PowerAdcStat
#define CoprocStat_payload_versionStat_MSGTYPE CoprocStat_VersionStat

#define CoprocStat_ButtonsStat_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UENUM,    buttonsPressed,    1)
#define CoprocStat_ButtonsStat_CALLBACK NULL
#define CoprocStat_ButtonsStat_DEFAULT NULL

#define CoprocStat_UltrasoundStat_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   utsIndex,          1) \
X(a, STATIC,   SINGULAR, UINT32,   roundtripMicrosecs,   2)
#define CoprocStat_UltrasoundStat_CALLBACK NULL
#define CoprocStat_UltrasoundStat_DEFAULT NULL

#define CoprocStat_MotorStat_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   motorIndex,        1) \
X(a, STATIC,   SINGULAR, UENUM,    mode,              2) \
X(a, STATIC,   SINGULAR, SINT32,   power,             3) \
X(a, STATIC,   SINGULAR, SINT32,   velocity,          4) \
X(a, STATIC,   SINGULAR, SINT32,   position,          5)
#define CoprocStat_MotorStat_CALLBACK NULL
#define CoprocStat_MotorStat_DEFAULT NULL

#define CoprocStat_PowerAdcStat_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   vccMv,             1) \
X(a, STATIC,   SINGULAR, UINT32,   battMidMv,         2) \
X(a, STATIC,   SINGULAR, INT32,    temperatureC,      3)
#define CoprocStat_PowerAdcStat_CALLBACK NULL
#define CoprocStat_PowerAdcStat_DEFAULT NULL

#define CoprocStat_VersionStat_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, FIXED_LENGTH_BYTES, revision,          1) \
X(a, STATIC,   SINGULAR, UINT32,   number,            2) \
X(a, STATIC,   SINGULAR, BOOL,     dirty,             3)
#define CoprocStat_VersionStat_CALLBACK NULL
#define CoprocStat_VersionStat_DEFAULT NULL

extern const pb_msgdesc_t None_msg;
extern const pb_msgdesc_t RegCoefs_msg;
extern const pb_msgdesc_t CoprocReq_msg;
extern const pb_msgdesc_t CoprocReq_SetLeds_msg;
extern const pb_msgdesc_t CoprocReq_GetButtons_msg;
extern const pb_msgdesc_t CoprocReq_SetStupidServo_msg;
extern const pb_msgdesc_t CoprocReq_UltrasoundReq_msg;
extern const pb_msgdesc_t CoprocReq_MotorReq_msg;
extern const pb_msgdesc_t CoprocReq_BuzzerReq_msg;
extern const pb_msgdesc_t CoprocReq_CalibratePower_msg;
extern const pb_msgdesc_t CoprocStat_msg;
extern const pb_msgdesc_t CoprocStat_ButtonsStat_msg;
extern const pb_msgdesc_t CoprocStat_UltrasoundStat_msg;
extern const pb_msgdesc_t CoprocStat_MotorStat_msg;
extern const pb_msgdesc_t CoprocStat_PowerAdcStat_msg;
extern const pb_msgdesc_t CoprocStat_VersionStat_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define None_fields &None_msg
#define RegCoefs_fields &RegCoefs_msg
#define CoprocReq_fields &CoprocReq_msg
#define CoprocReq_SetLeds_fields &CoprocReq_SetLeds_msg
#define CoprocReq_GetButtons_fields &CoprocReq_GetButtons_msg
#define CoprocReq_SetStupidServo_fields &CoprocReq_SetStupidServo_msg
#define CoprocReq_UltrasoundReq_fields &CoprocReq_UltrasoundReq_msg
#define CoprocReq_MotorReq_fields &CoprocReq_MotorReq_msg
#define CoprocReq_BuzzerReq_fields &CoprocReq_BuzzerReq_msg
#define CoprocReq_CalibratePower_fields &CoprocReq_CalibratePower_msg
#define CoprocStat_fields &CoprocStat_msg
#define CoprocStat_ButtonsStat_fields &CoprocStat_ButtonsStat_msg
#define CoprocStat_UltrasoundStat_fields &CoprocStat_UltrasoundStat_msg
#define CoprocStat_MotorStat_fields &CoprocStat_MotorStat_msg
#define CoprocStat_PowerAdcStat_fields &CoprocStat_PowerAdcStat_msg
#define CoprocStat_VersionStat_fields &CoprocStat_VersionStat_msg

/* Maximum encoded size of messages (where known) */
#define None_size                                0
#define RegCoefs_size                            18
#define CoprocReq_size                           29
#define CoprocReq_SetLeds_size                   2
#define CoprocReq_GetButtons_size                0
#define CoprocReq_SetStupidServo_size            11
#define CoprocReq_UltrasoundReq_size             8
#define CoprocReq_MotorReq_size                  27
#define CoprocReq_BuzzerReq_size                 2
#define CoprocReq_CalibratePower_size            24
#define CoprocStat_size                          25
#define CoprocStat_ButtonsStat_size              2
#define CoprocStat_UltrasoundStat_size           12
#define CoprocStat_MotorStat_size                26
#define CoprocStat_PowerAdcStat_size             23
#define CoprocStat_VersionStat_size              18

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
