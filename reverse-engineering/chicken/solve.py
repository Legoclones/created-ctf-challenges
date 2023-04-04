lines = open("chicken.chn").read().split("\n")
commands = []

for line in lines:
    commands.append(len(line.split(" ")))

flag = "!"*50
stack = []

for com in commands:
    # cast to int
    com = int(com)

    # push num onto stack
    if com >= 10:
        stack.append(com-10)

    # pop 2 nums from stack, add, and push back on
    elif com == 2:
        val1 = stack.pop()
        val2 = stack.pop()
        stack.append(val1+val2)

    # pop 2 nums from stack, subtract, and push back on
    elif com == 3:
        val1 = stack.pop()
        val2 = stack.pop()
        stack.append(val2-val1)

    # pop 2 nums from stack, multiply, and push back on
    elif com == 4:
        val1 = stack.pop()
        val2 = stack.pop()
        stack.append(val1*val2)

    # takes the index at the top of the stack and stores the character at that index
    elif com == 7:
        index = stack.pop()
        char = stack.pop()
        flag = flag[:index] + char + flag[index+1:]

    # takes the number from the top of the stack and converts it into ASCII
    elif com == 9:
        num = stack.pop()
        stack.append(chr(num))

    else:
        print("Unknown opcode -", com)

print(flag)