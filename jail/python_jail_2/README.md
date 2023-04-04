# Python Jail 2
**Level**: Medium

**Points**: 442

**Author**: Micheal Erickson and Justin Applegate

**Writeup by**: Noah Walker

**Description**:
```markdown
If you didn't have a period in your solution, I guess you're in luck!

`nc byuctf.xyz 40001`

[jail1.py]
```

## Writeup
The Python Jail series consists of 4 challenges revolve around a set of Python 3 scripts, in which the goal is to pass a Python expression over netcat that will extract the flags stored on the server. These flags are printed to stdout, and it happens that all stdout from the program is piped back to us.

Let's take a look at the code for Python Jail 1 (the simplest):

```python
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
```

Looks like we can't use a very direct method (sending `1337`), but we can call whatever functions we want (outside of `exec` and the keyword `class`). So, let's circumvent the conditional completely and send `print(FLAG)`.

Very cool! We can skip Jail 2 because the exact same thing works.

```python
print(FLAG)
ctf{h4h4_i_bet_you_h4te_python_now}
wrong
```

**Flag** - `ctf{h4h4_i_bet_you_h4te_python_now}`

## Real-World Application
Bypassing filters is a common challenge for exploits. Most RCE or SQL Injection payloads rely on some method of encoding to avoid being filtered out by WAFs and the like. Thus, by learning how to bypass filters, we can better develop effective exploits as a red team or patch discovered vulnerabilities as a blue team.

Thanks for reading!

## Notes

**Other possible solutions**:
```python
int('1' '3' '3' '7')
int('1a3a3a7'[::2])
len('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
```

## Hosting
This challenge should be a Docker container that runs the jail2.py file whenever someone connects to port 40001. All the proper files are included in here. The command to build the docker container is:

`sudo docker build -t jail2 .`

The command to start the challenge is:

`sudo docker run -p 40001:40000 jail2:latest`

The command to stop the challenge (since CTRL+C won't work) is:

`sudo docker stop jail2`