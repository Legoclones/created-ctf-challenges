# put the bytes from the TCP payload sending the key below as hex
payload1 = '484c494f53305553012b001100000001823772e56c611591523508c9b5aa0a61'

# put the bytes from the TCP payload sending the information below as hex
payload2 = '484c494f53305553015900f0000000df39368a61f6f160ec272867a5ee58d0354072ec4ddbde06da08d55b49a85c193dc12bba14e7bd5ef40aea036fac02f0facb319dffa226a7ccb13979bbb242b61598cf55a9b49444fdf1827934efd404d5f9fecdc4ac83927729f159b277c514df2b9fd1aed7b6b6812f92e524a82fdac85f89730fc4c4cb0a7cb01edce72d4ab378b8bcd6d488e56b228e5d586a71789941e2f6d0324f3febaabb709ff91933859bc10162e0e9a590b0de9cd27270dd04cea2196c41c35850196e54187a3f0273cd12cd88e2320ab4f7ec3ddce096d5888da3e9c9f6497bd5ac38e45ea34787e321694cee68886d380cdc5b209490ab'


### DON'T TOUCH ANYTHING BELOW THIS LINE ###
import xxtea, subprocess, binascii

# helper function
def deobfuscate(b_arr : bytes):
    retval = bytearray(16)
    for i in range(4):
        retval[i] = b_arr[3 - i]
        retval[i + 4] = b_arr[7 - i]
        retval[i + 8] = b_arr[11 - i]
        retval[i + 12] = b_arr[15 - i]
    return bytes(retval)

# get payload for Java file
original_key = b'routerLocalWhoAr'
bytes_from_server = bytes.fromhex(payload1)[16:]
arg = binascii.hexlify(deobfuscate(bytes_from_server)).decode('utf-8')

# subprocess
out = subprocess.getoutput(f'javac pain.java && java pain {arg}')

# get output
new_key = deobfuscate(bytes.fromhex(out))
second_payload = bytes.fromhex(payload2)[15:]
print(xxtea.decrypt(second_payload, new_key))