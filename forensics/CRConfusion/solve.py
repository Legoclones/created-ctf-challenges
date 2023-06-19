import string

# read in and parse data
lines1 = open("crc1.txt").read().splitlines()
lines2 = open("crc2.txt").read().splitlines()
lines3 = open("crc3.txt").read().splitlines()

assert(len(lines1) == len(lines2))

data = []
for i in range(len(lines1)):
    obj = {
        "orig1": lines1[i].split(" --> ")[0],
        "crc1": lines1[i].split(" --> ")[1],
        "orig2": lines2[i].split(" --> ")[0],
        "crc2": lines2[i].split(" --> ")[1],
        "orig3": lines3[i].split(" --> ")[0],
        "crc3": lines3[i].split(" --> ")[1],
    }
    data.append(obj)


# function to calculate the 8-bit CRC
def crc8(data : str, polynomial : int):
    data += "00000000"

    for _ in range(len(data)-8):
        msb = data[0]
        data = data[1:]

        if msb != "0":
            beginning = int(data[:8],2)
            end = data[8:]

            beginning ^= polynomial

            data = bin(beginning)[2:].zfill(8) + end
    return data


# brute force flag letters
flag = ""
for obj in data:
    for s in string.printable:
        poly = ord(s)
        if (crc8(obj["orig1"], poly) == obj["crc1"]) and (crc8(obj["orig2"], poly) == obj["crc2"]) and (crc8(obj["orig3"], poly) == obj["crc3"]):
            flag += chr(poly)
            print(flag)
            break