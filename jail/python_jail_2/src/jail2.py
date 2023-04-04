import re

from answer import FLAG

regexes = [
    # only change is that periods are now disallowed
    r'\.',
    
    r'\d\d',
    r'\+',
    r'-',
    r'\*',
    r'/',
    r'<',
    r'>',
    r'\^',
    r'v',
    r'&',
    r'\|',
    r'"',
    r'%',
    r'_',
    r'[\U000000ff-\U0010ffff]',
    r'exec'
]

inp = input('>>> ')

if any([re.search(r, inp) for r in regexes]):
    print("Don't do bad stuff")
    exit()

if eval(inp) == 1337:
    print(FLAG)
else:
    print('wrong')