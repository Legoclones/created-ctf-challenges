# OPCODES
LOAD = 0x1
INPUT = 0x2
PRINT = 0x3
ADD = 0x4
SUB = 0x5
MUL = 0x6
XOR = 0x7
CMP = 0x8


# Stack and instructions
STACK = []
instructions = open("instructions.bin",'rb').read()


# get the input from the user of a length specified by the bin file
length = instructions[0]
inp = input("Enter the flag: ")
if len(inp) != length:
    print("Incorrect")
    exit()
inp = inp[:length]
nums = []

for letter in inp:
    nums.append(ord(letter))

print("LENGTH: ", length)


# loop through the instructions
i = 1
input_counter = 0
while i < len(instructions):
    inst = instructions[i]

    if inst == LOAD:
        print("Loading",instructions[i+1],"to the stack")
        STACK.append(instructions[i+1])
        i += 2

    elif (inst == INPUT) and (input_counter < length):
        print("Loading",nums[input_counter],"from input to the stack")
        STACK.append(nums[input_counter])
        input_counter += 1
        i += 1

    elif inst == PRINT:
        tmp = STACK.pop()
        print("Printing",tmp)
        i += 1
        
    elif inst == ADD:
        val1 = STACK.pop()
        val2 = STACK.pop()
        print("Adding",val1,"and",val2)
        STACK.append(val1 + val2)
        i += 1
        
    elif inst == SUB:
        val1 = STACK.pop()
        val2 = STACK.pop()
        print("Subtracting",val1,"and",val2)
        STACK.append(val1 - val2)
        i += 1
        
    elif inst == MUL:
        val1 = STACK.pop()
        val2 = STACK.pop()
        print("Multiplying",val1,"and",val2)
        STACK.append(val1 * val2)
        i += 1
        
    elif inst == XOR:
        val1 = STACK.pop()
        val2 = STACK.pop()
        print("XORing",val1,"and",val2)
        STACK.append(val1 ^ val2)
        i += 1

    elif inst == CMP:
        output = STACK.pop()
        if output == 0:
            print("Correct!")
            i += 1
        else:
            print("Incorrect!")
            exit()

    else:
        print("Invalid instruction")
        exit()

print("Completed")