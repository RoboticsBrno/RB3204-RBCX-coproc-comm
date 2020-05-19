#!/bin/sh

# Install protobuf-compiler and pip3 install nanopb

nanopb_generator -D src rbcx.proto
protoc --python_out=tools/pb rbcx.proto
