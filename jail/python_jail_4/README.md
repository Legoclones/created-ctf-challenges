# Python Jail 4
**Level**: Hard

**Points**: 647

**Author**: Micheal Erickson and Justin Applegate

**Writeup by**: Noah Walker

**Description**:
```markdown
And for the final stage, a length constraint - have fun!!

nc byuctf.xyz 40003

[jail4.py]
```

## Writeup
The Python Jail series consists of 4 challenges revolve around a set of Python 3 scripts, in which the goal is to pass a Python expression over netcat that will extract the flags stored on the server. These flags are printed to stdout, and it happens that all stdout from the program is piped back to us.

Let's take a look at the code for Python Jail 4:

```python
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
```

At first glance, this doesn't look all that menacing. That's until noticing the length restriction of 8. This means none of our past solutions will work immediately. However, Unicode characters are no longer filtered out in this Jail. That leaves a surprisingly simple solution. In the Python REPL, we can get a character mapping to 1337.

```python
>>> chr(1337)
'Թ'
>>> ord('Թ')
1337
```

And it so happens that `ord('Թ')` is precisely 8 characters. Sending this to the server for Python Jail 4 nets us our last flag of the series. I've heard that the intended solution to Jail 4 is `1_3_3_7`, which is only 7 characters. This is because Python allows underscores in numbers for formatting, and will interpret this without underscores. Hence, we've successfully solved the Python Jails the wrong way.

**Flag** - `ctf{s0rry}`

## Real-World Application
Bypassing filters is a common challenge for exploits. Most RCE or SQL Injection payloads rely on some method of encoding to avoid being filtered out by WAFs and the like. Thus, by learning how to bypass filters, we can better develop effective exploits as a red team or patch discovered vulnerabilities as a blue team.

Thanks for reading!

## Hosting
This challenge should be a Docker container that runs the jail4.py file whenever someone connects to port 40003. All the proper files are included in here. The command to build the docker container is:

`sudo docker build -t jail4 .`

The command to start the challenge is:

`sudo docker run -p 40003:40000 jail4:latest`

The command to stop the challenge (since CTRL+C won't work) is:

`sudo docker stop jail4`