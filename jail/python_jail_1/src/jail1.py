import re

# We have a file on our server called answer.py with the flag stored. In order to
# read it, you must type in Python code that evaluates to 1337
from answer import FLAG

# these are all the characters or symbols you can't use - you must write Python code that equals 1337 WITHOUT these
regexes = [
    # no two digits in a row (aka 13 and 37 will be caught)
    r'\d\d',

    # no common math symbols
    r'\+',
    r'-',
    r'\*',
    r'/',

    # we've removed other characters
    r'<',
    r'>',
    r'\^',
    r'v',
    r'&',
    r'\|',
    r'_',
    r'%',

    # blocks all Unicode symbols and 'exec' and 'class' to prevent unwanted RCE
    r'[\U000000ff-\U0010ffff]',
    r'exec',
    r'class'
]

inp = input('>>> ')

if any([re.search(r, inp) for r in regexes]):
    print("Don't do bad stuff")
    exit()

if eval(inp) == 1337:
    print(FLAG)
else:
    print('wrong')