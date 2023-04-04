LOAD = 0x1
INPUT = 0x2
PRINT = 0x3
A1d = 0x4
SUB = 0x5
MUL = 0x6
XOR = 0x7
CMP = 0x8

LENGTH = 49
FLAG = 'byuctf{vms_just_1mplem3nt_0pcodes_&_instruct10n5}'

instructions = [
    LOAD, ord('b'), INPUT, SUB, CMP, 
    LOAD, ord('y'), INPUT, SUB, CMP, 
    LOAD, ord('u'), INPUT, SUB, CMP, 
    LOAD, ord('c'), INPUT, SUB, CMP, 
    LOAD, ord('t'), INPUT, SUB, CMP, 
    LOAD, ord('f'), INPUT, SUB, CMP, 
    LOAD, 0x98, INPUT, XOR, LOAD, ord('{')^0x98, SUB, CMP,
    LOAD, 0xe7, INPUT, XOR, LOAD, ord('v')^0xe7, SUB, CMP,
    LOAD, 0x5d, INPUT, XOR, LOAD, ord('m')^0x5d, SUB, CMP,
    LOAD, 0x4d, INPUT, XOR, LOAD, ord('s')^0x4d, SUB, CMP,
    LOAD, 0xa6, INPUT, XOR, LOAD, ord('_')^0xa6, SUB, CMP,
    LOAD, 0xb8, INPUT, XOR, LOAD, ord('j')^0xb8, SUB, CMP,
    LOAD, 0x10, INPUT, SUB, LOAD, ord('u')-0x10, SUB, CMP,
    LOAD, 0x1b, INPUT, SUB, LOAD, ord('s')-0x1b, SUB, CMP,
    LOAD, 0x12, INPUT, SUB, LOAD, ord('t')-0x12, SUB, CMP,
    LOAD, 0x9, INPUT, SUB, LOAD, ord('_')-0x9, SUB, CMP,
    LOAD, 0x1d, INPUT, SUB, LOAD, ord('1')-0x1d, SUB, CMP,
    LOAD, 0x8, INPUT, SUB, LOAD, ord('m')-0x8, SUB, CMP,
    LOAD, 0x5, INPUT, SUB, LOAD, ord('p')-0x5, SUB, CMP,
    LOAD, 0x1d, INPUT, SUB, LOAD, ord('l')-0x1d, SUB, CMP,
    LOAD, 0x9, INPUT, A1d, LOAD, ord('e')+0x9, SUB, CMP,
    LOAD, 0xf, INPUT, A1d, LOAD, ord('m')+0xf, SUB, CMP,
    LOAD, 0x7, INPUT, A1d, LOAD, ord('3')+0x7, SUB, CMP,
    LOAD, 0xd, INPUT, A1d, LOAD, ord('n')+0xd, SUB, CMP,
    LOAD, 0x1, INPUT, A1d, LOAD, ord('t')+0x1, SUB, CMP,
    LOAD, 0x8, INPUT, A1d, LOAD, ord('_')+0x8, SUB, CMP,
    LOAD, 0xa, INPUT, A1d, LOAD, ord('0')+0xa, SUB, CMP,
    LOAD, 0xb, INPUT, A1d, LOAD, ord('p')+0xb, SUB, CMP,
    LOAD, 0x5, INPUT, A1d, LOAD, ord('c')+0x5, SUB, CMP,
    LOAD, 0x5, INPUT, A1d, LOAD, ord('o')+0x5, SUB, CMP,
    LOAD, 0x13, INPUT, A1d, LOAD, ord('d')+0x13, SUB, CMP,
    LOAD, ord('e'), INPUT, SUB, CMP, 
    LOAD, ord('s'), INPUT, SUB, CMP, 
    LOAD, ord('_'), INPUT, SUB, CMP, 
    LOAD, ord('&'), INPUT, SUB, CMP, 
    LOAD, ord('_'), INPUT, SUB, CMP, 
    LOAD, ord('i'), INPUT, SUB, CMP, 
    LOAD, 0x10, INPUT, SUB, LOAD, ord('n')-0x10, SUB, CMP,
    LOAD, 0x1b, INPUT, SUB, LOAD, ord('s')-0x1b, SUB, CMP,
    LOAD, 0x12, INPUT, SUB, LOAD, ord('t')-0x12, SUB, CMP,
    LOAD, 0x9, INPUT, SUB, LOAD, ord('r')-0x9, SUB, CMP,
    LOAD, 0x1d, INPUT, SUB, LOAD, ord('u')-0x1d, SUB, CMP,
    LOAD, 0x8, INPUT, SUB, LOAD, ord('c')-0x8, SUB, CMP,
    LOAD, 0x5, INPUT, SUB, LOAD, ord('t')-0x5, SUB, CMP,
    LOAD, 0x1d, INPUT, SUB, LOAD, ord('1')-0x1d, SUB, CMP,
    LOAD, 0x12, INPUT, A1d, LOAD, ord('0')+0x12, SUB, CMP,
    LOAD, 0x9, INPUT, A1d, LOAD, ord('n')+0x9, SUB, CMP,
    LOAD, 0x2, INPUT, A1d, LOAD, ord('5')+0x2, SUB, CMP,
    LOAD, 0x1, INPUT, A1d, LOAD, ord('}')+0x1, SUB, CMP,
]

bts = []
for val in instructions:
    bts.append(val.to_bytes(1, byteorder='little'))

full = b''.join(bts)

with open('instructions.bin', 'wb') as f:
    f.write(LENGTH.to_bytes(1, byteorder='little'))
    f.write(full)