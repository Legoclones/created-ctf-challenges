lines = open('vilo_boot.csv','r').read().split('\n')[1:]
code_sections = []
fs = [0]*(0xffffff+4)
total_data_str = b''


# parse CSV
data1 = []
data2 = []
for line in lines:
    sections = line.split(',')

    if len(sections) > 1 and sections[1] == '"disable"':
        code_sections.append((b''.join([int.to_bytes(x) for x in data1]), b''.join([int.to_bytes(x) for x in data2])))
        data1 = []
        data2 = []

    if len(sections) > 1 and sections[1] == '"result"':
        data1.append(int(sections[2],16))
        data2.append(int(sections[3],16))

print(code_sections[1])

# parse instructions
for s in code_sections:
    bin = s[0]
    instr = s[1]

    if len(instr) == 0:
        continue
    mode = instr[0]

    if mode == 3:
        # read
        addr = instr[1:4]
        data = bin[4:]

        total_data_str += data

        for i in range(len(data)):
            fs[int.from_bytes(addr)+i] = data[i]

fs = b''.join([int.to_bytes(x) for x in fs])

with open('fs.bin','wb') as f:
    f.write(fs)

with open('data.bin','wb') as f:
    f.write(total_data_str)