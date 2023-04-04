import re

from answer import FLAG

regexes = [
    r'\d\d',
    r'\.',
    r'\+',
    r'-',
    r'\*',
    r'/',
    r'>',
    r'v',
    r'"',
    r"'",
    r'\(',
    r'_',
    r'[\U000000ff-\U0010ffff]',
]

inp = input('>>> ')

if any([re.search(r, inp) for r in regexes]):
    print("Don't do bad stuff")
    exit()

if eval(inp) == 1337:
    print(FLAG)
else:
    print('wrong')