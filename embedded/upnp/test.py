import upnpy
import sys
import base64
import struct

# Print decoded device info 
def print_device_info(service):
    device_info = service.GetDeviceInfo()['NewDeviceInfo'].encode()

    info = base64.b64decode(device_info)
    print(info)
    print("\n\nDevice Info:")
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

upnp = upnpy.UPnP()

# Discover UPnP devices on the network
devices = upnp.discover(ip_address="192.168.58.1")

# Exit if no devices found
if len(devices) == 0:
    print("No devices found")
    sys.exit(1)

# Choose first device
device = devices[0]

# Get and print the services available for this device
services = device.get_services()
print("SERVICES")
# print(services)
for service in services:
    # Get and print the actions for each service
    actions = service.get_actions()
    print(f"ACTIONS FOR {service}")
    # print(actions)
    for action in actions:
        print(action.name)
        in_arguments = action.get_input_arguments()
        out_arguments = action.get_output_arguments()
        # print(action.arguments[0].name)
        # print(action.arguments[0].direction)
        # print(action.arguments[0].return_value)
        # print(action.arguments[0].related_state_variable)
        print("INPUT ARGUMENTS:")
        if in_arguments:
            for in_argument in in_arguments:
                print(" -", in_argument)
        else:
            print(" - none")

        print("OUTPUT ARGUMENTS:")
        if out_arguments:
            for out_argument in out_arguments:
                print(" -", out_argument)
        else:
            print(" - none")

        print()
    
    # Get device info
    print(print_device_info(service))