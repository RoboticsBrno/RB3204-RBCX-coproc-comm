#pragma once

#include <array>
#include <stddef.h>
#include <stdint.h>
#include <pb.h>

namespace rb {

class CoprocCodec {
    std::array<uint8_t, 254> m_pb_enc_arena;
    std::array<uint8_t, 254> m_pb_dec_arena;

public:
    size_t encode(const pb_msgdesc_t* fields, const void* src_struct, uint8_t* buf, size_t size);
    bool decode(const uint8_t* buf, size_t size, const pb_msgdesc_t* fields, void* dest_struct);
};

};
