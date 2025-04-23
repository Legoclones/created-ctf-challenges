import sys
import base64
import struct

info = open('./msg.bin', 'rb').read()
print("Device Info:")
while info:
    try:
        type, length = struct.unpack('!HH', info[:4])
        value = struct.unpack('!%is'%length, info[4:4+length])[0]
        info = info[4+length:]

        if type == 0x1023:
            print('\tModel Name: %s' % value)
        elif type == 0x1021:
            print('\tManufacturer: %s' % value)
        elif type == 0x1011:
            print('\tDevice Name: %s' % value)
        elif type == 0x1020:
            pretty_mac = ':'.join('%02x' % v for v in value)
            print('\tMAC Address: %s' % pretty_mac)
        elif type == 0x1032:
            encoded_pk = base64.b64encode(value)
            print('\tPublic Key: %s' % encoded_pk)
        elif type == 0x101a:
            encoded_nonce = base64.b64encode(value)
            print('\tNonce: %s' % encoded_nonce)
        elif type == 0x104a:
            print('\tVersion: %s' % value)
        elif type == 0x1022:
            print('\tMessage Type: %s' % value)
        elif type == 0x1047:
            print('\tUUID_E: %s' % value)
        elif type == 0x1004:
            print('\tAuth Type Flags: %s' % value)
        elif type == 0x1010:
            print('\tEncr Type Flags: %s' % value)
        elif type == 0x100d:
            print('\tConn Type Flags: %s' % value)
        elif type == 0x1008:
            print('\tConfig Methods: %s' % value)
        elif type == 0x1044:
            print('\tSC State: %s' % value)
        elif type == 0x1024:
            print('\tModel Number: %s' % value)
        elif type == 0x1042:
            print('\tSerial Number: %s' % value)
        elif type == 0x1054:
            print('\tPrim Dev Type: %s' % value)
        elif type == 0x103c:
            print('\tRF Band: %s' % value)
        elif type == 0x1002:
            print('\tAssoc State: %s' % value)
        elif type == 0x1012:
            print('\tDevice Pwd ID: %s' % value)
        elif type == 0x1009:
            print('\tConfig Error: %s' % value)
        elif type == 0x102d:
            print('\tOS Version: %s' % value)
        elif type == 0x1049:
            print('\tVendor Ext: %s' % value)
        else:
            print(hex(type),value)
    except Exception as e: 
        print("Failed TLV parsing",e)
        print(info[:20])
        sys.exit(1)