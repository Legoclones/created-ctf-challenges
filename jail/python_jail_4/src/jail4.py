import re

from answer import FLAG

regexes = [
    r'\d\d',
    r'\+',
    r'-',
    r'\*',
    r'/',
]

inp = input('>>> ')

if any([re.search(r, inp) for r in regexes]) or (len(inp) > 8):
    print("Don't do bad stuff")
    exit()

if eval(inp) == 1337:
    print(FLAG)
else:
    print('wrong')