#include <pb_decode.h>
#include <pb_encode.h>

#include "cobs/cobs.h"
#include "coproc_msg.h"

namespace rb {

bool CoprocMsg::encode(const pb_msgdesc_t* fields, const void* src_struct, std::vector<uint8_t>& output) {
    size_t encodedSize = 0;
    if (!pb_get_encoded_size(&encodedSize, fields, src_struct)) {
        // TODO: how to report errors?
        return false;
    }

    std::vector<uint8_t> pb_data(encodedSize);

    auto ostream = pb_ostream_from_buffer(pb_data.data(), encodedSize);
    if (!pb_encode(&ostream, fields, src_struct)) {
        // TODO: how to report errors?
        return false;
    }
    pb_data.resize(ostream.bytes_written);

    output.resize(COBS_ENCODE_DST_BUF_LEN_MAX(pb_data.size()));
    const auto cobs_res = cobs_encode(output.data(), output.size(), pb_data.data(), pb_data.size());
    if (cobs_res.status != COBS_ENCODE_OK) {
        // TODO: how to report errors?
        return false;
    }
    output.resize(cobs_res.out_len);

    if (cobs_res.out_len > 0xFF) {
        // TODO: how to report errors?
        return false;
    }

    return true;
}

bool CoprocMsg::decode(const uint8_t* buf, size_t size, const pb_msgdesc_t* fields, void* dest_struct) {
    std::vector<uint8_t> pb_data(COBS_DECODE_DST_BUF_LEN_MAX(size));
    auto cobs_res = cobs_decode(pb_data.data(), pb_data.size(), buf, size);
    if (cobs_res.status != COBS_DECODE_OK) {
        // TODO: how to report errors?
        return false;
    }
    pb_data.resize(cobs_res.out_len);

    auto istream = pb_istream_from_buffer(pb_data.data(), pb_data.size());
    return pb_decode(&istream, fields, dest_struct);
}

};
