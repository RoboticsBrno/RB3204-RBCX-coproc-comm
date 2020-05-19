#pragma once

#include <vector>

#include <pb.h>

namespace rb {

class CoprocMsg {
public:
    static bool encode(const pb_msgdesc_t* fields, const void* src_struct, std::vector<uint8_t>& output);
    static bool decode(const uint8_t* buf, size_t size, const pb_msgdesc_t* fields, void* dest_struct);
};

};
