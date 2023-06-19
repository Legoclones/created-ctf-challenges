from pwn import *

#p = process('src/chall.py')
p = remote('byuctf.xyz', 40014)


# helper functions
def roman_to_int(dat):
        s = dat.replace("1000","M").replace("500","D").replace("100","C").replace("50","L").replace("10","X").replace("5","V"). replace("1","I")
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

def num_to_roman(number):
    retval = ""
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
     
    while number:
        div = number // num[i]
        number %= num[i]
 
        while div:
            retval += sym[i]
            div -= 1
        i -= 1

    return retval.replace("I","1").replace("V","5").replace("X","10").replace("L","50").replace("C","100").replace("D","500").replace("M","1000")


# get intial intro
p.recvline()

# get 200 problems
for i in range(500):
    # get problem
    problem = p.recvuntil(b"=").decode('utf-8').strip()
    print(problem,end=' ')

    # parse problem
    problem = problem.split()
    num1 = roman_to_int(problem[0])
    num2 = roman_to_int(problem[2])
    operation = problem[1]

    # solve problem
    if operation == '+':
        answer = num1 + num2
    elif operation == '*':
        answer = num1 * num2

    # send answer
    print(num_to_roman(answer))
    p.sendline(num_to_roman(answer))

p.interactive()