import random

flag = "byuctf{cyclic_redundancy_checks_are_used_to_detect_errors_in_data_transmission}"

for letter in flag:
    orig = bin(random.randint(0,2**32))[2:].zfill(32)
    data = orig + "00000000"

    for _ in range(len(data)-8):
        msb = data[0]
        data = data[1:]

        if msb != "0":
            beginning = int(data[:8],2)
            end = data[8:]

            beginning ^= ord(letter)

            data = bin(beginning)[2:].zfill(8) + end
    print(orig,"-->",data)