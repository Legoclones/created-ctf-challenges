# Python Jail 3
**Level**: Hard

**Points**: 636

**Author**: Micheal Erickson and Justin Applegate

**Writeup by**: Noah Walker

**Description**:
```markdown
Now, it's all about numbersssss!!! No strings allowed!!

nc byuctf.xyz 40002

[jail3.py]
```

## Writeup
The Python Jail series consists of 4 challenges revolve around a set of Python 3 scripts, in which the goal is to pass a Python expression over netcat that will extract the flags stored on the server. These flags are printed to stdout, and it happens that all stdout from the program is piped back to us.

Let's take a look at the code for Python Jail 3:

```python
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
```

Well, with left parenthesis gone, looks like our function-calling days are over. However, we received a new mathematical operation: `^`, which is XOR in Python. We still need a way of getting our operands to not contain consecutive digits. With Python's native prefix for hexidecimal numbers, maybe we can find a stable hexidecimal expression for 1337. Opening the Python REPL, let's look at 1337 directly.

```python
>>> hex(1337)
'0x539'
```

Hmm, that will not do. But with XOR, maybe we can get something useful. Let's take that expression and calculate XOR with `0xfff` on the left-hand side.

```python
>>> hex(0xfff^0x539)
'0xac6'
```

Perfect! That means we have

```python
>>> 0xfff^0xac6
1337
```

Send that expression to Jail 3, and we have our flag!

**Flag** - `ctf{we_c0ns1dered_putt1ng_th1s_1n_a_self-l0ath1ng_categ0ry}`

## Real-World Application
Bypassing filters is a common challenge for exploits. Most RCE or SQL Injection payloads rely on some method of encoding to avoid being filtered out by WAFs and the like. Thus, by learning how to bypass filters, we can better develop effective exploits as a red team or patch discovered vulnerabilities as a blue team.

Thanks for reading!

## Notes

**Other possible solutions**:

```python
0xad9 % 0x5a0
1<<9<<1|1<<8|1<<5|1<<4|1<<3|1
```

## Hosting
This challenge should be a Docker container that runs the jail3.py file whenever someone connects to port 40002. All the proper files are included in here. The command to build the docker container is:

`sudo docker build -t jail3 .`

The command to start the challenge is:

`sudo docker run -p 40002:40000 jail3:latest`

The command to stop the challenge (since CTRL+C won't work) is:

`sudo docker stop jail3`