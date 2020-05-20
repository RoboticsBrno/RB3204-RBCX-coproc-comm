#include <pb_decode.h>
#include <pb_encode.h>

#include "cobs/cobs.h"
#include "coproc_codec.h"

namespace rb {

size_t CoprocCodec::encode(const pb_msgdesc_t* fields, const void* src_struct, uint8_t* buf, size_t size) {
    size_t encoded_size = 0;
    if (!pb_get_encoded_size(&encoded_size, fields, src_struct) || encoded_size > m_pb_enc_arena.size()) {
        // TODO: how to report errors?
        return 0;
    }

    auto ostream = pb_ostream_from_buffer(m_pb_enc_arena.data(), m_pb_enc_arena.size());
    if (!pb_encode(&ostream, fields, src_struct)) {
        // TODO: how to report errors?
        return 0;
    }

    const auto cobs_res = cobs_encode(buf, size, m_pb_enc_arena.data(), encoded_size);
    if (cobs_res.status != COBS_ENCODE_OK) {
        // TODO: how to report errors?
        return 0;
    }
    if (cobs_res.out_len > 0xFF) {
        // TODO: how to report errors?
        return 0;
    }

    return true;
}

bool CoprocCodec::decode(const uint8_t* buf, size_t size, const pb_msgdesc_t* fields, void* dest_struct) {
    auto cobs_res = cobs_decode(m_pb_dec_arena.data(), m_pb_dec_arena.size(), buf, size);
    if (cobs_res.status != COBS_DECODE_OK) {
        // TODO: how to report errors?
        return false;
    }

    auto istream = pb_istream_from_buffer(m_pb_dec_arena.data(), m_pb_dec_arena.size());
    return pb_decode(&istream, fields, dest_struct);
}

};
