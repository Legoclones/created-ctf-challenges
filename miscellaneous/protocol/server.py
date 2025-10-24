#!/usr/local/bin/python3

### IMPORTS ###
import sys
from hashlib import md5



### CONSTANTS ###
FLAG = b"HC{bl1nd_pr0t0c0l_4n4lys1s_sucks_but_1s_necess4ry_s0met1m3s}"
FLAG_SEGMENT_1 = FLAG[:len(FLAG)//2]
FLAG_SEGMENT_2 = FLAG[len(FLAG)//2:]

DEBUG_MODE = False
DEBUG_MSG = b'pls gimme fleg'

ECHO_TYPE = 0x02
FLAG_TYPE = 0xc0
DEBUG_ENABLE_TYPE = 0xff
DEBUG_HANDLE_TYPE = 0x67




### RECEIVE DATA ###
data = sys.stdin.buffer.readline().rstrip(b"\n")

while data != b'':
    # ensure at least 3 bytes
    if len(data) < 3:
        print("Data too short")
        sys.exit(1)

    typ = data[0]
    length = int.from_bytes(data[1:3], 'little')
    payload = data[3:3+length]
    data = data[3+length:]



    ### CHECKS ###
    # check length
    if length != len(payload):
        print(f"Length 0x{length:04x} does not match payload size 0x{len(payload):04x}")
        sys.exit(1)

    # check type
    if typ not in (ECHO_TYPE, FLAG_TYPE, DEBUG_ENABLE_TYPE, DEBUG_HANDLE_TYPE):
        print(f"Unknown type 0x{typ:02x}")
        sys.exit(1)



    ### HANDLE TYPES ###
    if typ == ECHO_TYPE:
        # echo back the payload
        sys.stdout.buffer.write(b"Echo: "+payload)

    elif typ == FLAG_TYPE:
        if length != 0:
            print(f"Type 0x{FLAG_TYPE:02x} must have length 0")
            sys.exit(1)
        sys.stdout.buffer.write(FLAG_SEGMENT_1)

    elif typ == DEBUG_ENABLE_TYPE:
        if length != 0:
            print(f"Type 0x{DEBUG_ENABLE_TYPE:02x} must have length 0")
            sys.exit(1)
        DEBUG_MODE = True
        sys.stdout.buffer.write(b"Debug mode enabled")

    elif typ == DEBUG_HANDLE_TYPE:
        if not DEBUG_MODE:
            print("Debug mode not enabled")
            sys.exit(1)
        
        if len(payload) < 16:
            print("Debug message too short")
            sys.exit(1)

        # check hash
        received_hash = payload[-16:]
        actual_hash = md5(payload[:-16]).digest()

        if received_hash != actual_hash:
            print(f"MD5 hash of payload '{payload[:-16]}' does not match received hash 0x{received_hash.hex()}")
            sys.exit(1)

        # ensure message is correct
        if payload[:-16] != DEBUG_MSG:
            print(f"Debug message does not match '{DEBUG_MSG}'")
            sys.exit(1)

        sys.stdout.buffer.write(FLAG_SEGMENT_2)