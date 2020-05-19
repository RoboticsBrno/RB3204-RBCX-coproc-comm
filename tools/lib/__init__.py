import struct

from typing import IO
from google.protobuf.message import Message

from . import cobs

def frame_encode(msg: Message) -> bytes:
    pb_data = msg.SerializeToString()
    return cobs.encode(pb_data)

def frame_send(file: IO[bytes], msg: Message):
    data = frame_encode(msg)
    file.write(struct.pack("<BB", 0, len(data)))
    file.write(data)
