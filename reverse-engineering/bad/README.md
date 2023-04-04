# Bad
**Level**: Hard

**Points**: 647

**Author**: Justin Applegate

**Writeup by**: Justin Applegate

**Description**:
```markdown
This is the result of many hours of geeking out about Unicode :)

[bad.py]
```

## Writeup
Okay, I've made short little writeups about most problems, but this one and Web bad are two of my favorite challenges, so I'm going to take the time to make a complete step-by-step writeup for it. The goal of this problem is to reverse engineer the Python script and find a flag hidden somewhere. The code is:

```python
import base64;𝒾𝒻=[int('🯱🯶'),int('🯳🯳'),int('🯱🯹'),int('🯴🯰'),int('🯲🯲'),int('🯱🯲'),int('🯲🯵'),int('-🯳🯵'),int('🯳🯵'),int('🯱🯸'),int('🯱🯲'),int('🯳🯴'),int('🯲🯷'),int('🯲🯲'),int('🯱🯶'),int('-🯳🯵'),int('🯱🯷'),int('-🯳🯲'),int('🯱🯲'),int('🯱🯵'),int('🯱🯶'),int('🯱🯲'),int('🯳🯸'),int('-🯳🯵'),int('🯳🯴'),int('🯱🯲'),int('🯱🯶'),int('🯱🯴'),int('🯲🯷'),int('🯱🯲'),int('🯱🯷'),int('-🯳🯵'),int('🯱🯲'),int('🯳🯳'),int('🯲🯱'),int('-🯳🯲'),int('🯱🯲'),int('🯳🯲'),int('🯳🯳'),int('🯳🯴'),int('🯲🯹'),int('🯲🯲'),int('🯱🯷'),int('-🯳🯲'),int('🯳🯲'),int('🯳🯳'),int('🯱🯲'),int('🯳🯲'),int('🯳🯳'),int('🯳🯴'),int('🯱🯹'),int('🯱🯹'),int('🯴🯲')];ᵉₓᵉc('answer=input("Flag> ")');exec(base64.b32decode("NFTCA3DFNYUPBHMTVLYJ3E4D6COZRNHQTWKIB4E5SOXPBHMTXMUSCPLJNZ2CQJ7BU6LSOKJKNFXHIKBH36ECOKJNNFXHIKBH6CIYJOJHFE5AUIBAEAQGK6DFMMUGEYLTMU3DILTCGY2GIZLDN5SGKKBHLJMGQ3CZPFTW4Y2IJJYGE3SRN5EWW3DVLEZDS6LDNVLGUZCDJFYE6M2GGFQVQULPJNJWG4BHFEUQ===="));exec(base64.b64decode("Zm9yIPCdmZvwnZmk8J2ZpyBpbiByYW5nZShsZW4o8J2YovCdmK/wnZOI8J2YuPCdmKbwnZizKSk6CiAgICBpZiDwnZK+8J2Su1vwnZmb8J2ZpPCdmaddIT1vcmQo8J2StvCdk7fwnZO88J2TjPCdkZLwnZOHW/CdmZvwnZmk8J2Zp10pLWV2YWwoIlxVMDAwMDAwNjlcVTAwMDAwMDZFXFUwMDAwMDA3NFxVMDAwMDAwMjhcVTAwMDAwMDI3XFUwMDAwQTlGOVxVMDAwMDAwMjdcVTAwMDAwMDI5XFUwMDAwMDAyQVxVMDAwMDAwNjlcVTAwMDAwMDZFXFUwMDAwMDA3NFxVMDAwMDAwMjhcVTAwMDAwMDI3XFUwMDAwMEI2RVxVMDAwMDAwMjdcVTAwMDAwMDI5XFUwMDAwMDAyQlxVMDAwMDAwNjlcVTAwMDAwMDZFXFUwMDAwMDA3NFxVMDAwMDAwMjhcVTAwMDAwMDI3XFUwMDAwMEE2QVxVMDAwMDAwMjdcVTAwMDAwMDI5XFUwMDAwMDAyQlxVMDAwMDAwNjlcVTAwMDAwMDZFXFUwMDAwMDA3NFxVMDAwMDAwMjhcVTAwMDAwMDI3XFUwMDAwMDlFRFxVMDAwMDAwMjdcVTAwMDAwMDI5Iik6CiAgICAgICAgZXhlYyhiYXNlNjQuYjY0ZGVjb2RlKCdaWGhsWXlnbmNISnBiblFvSWtsdVkyOXljbVZqZENJcE8zRjFhWFFvS1NjcCcpKQ=="));print("Success!")
```

At first inspection, this is pretty gnarly! Some unreadable Unicode characters are being passed into the `int` function, `base64` and `base32` strings are decoded and being run, an odd version of `exec` is being run, and an italic variable named `𝒾𝒻` is initialized as an array. Running the script and inputting "what" gives the result:

```shell
$ python3 resolve.py 
Flag> what
Incorrect
```

After [base64](https://emn178.github.io/online-tools/base64_decode.html) and [base32](https://emn178.github.io/online-tools/base32_decode.html) decoding all of the lines of code present, this is what the script looks like:

```python
import base64

𝒾𝒻=[int('🯱🯶'),int('🯳🯳'),int('🯱🯹'),int('🯴🯰'),int('🯲🯲'),int('🯱🯲'),int('🯲🯵'),int('-🯳🯵'),int('🯳🯵'),int('🯱🯸'),int('🯱🯲'),int('🯳🯴'),int('🯲🯷'),int('🯲🯲'),int('🯱🯶'),int('-🯳🯵'),int('🯱🯷'),int('-🯳🯲'),int('🯱🯲'),int('🯱🯵'),int('🯱🯶'),int('🯱🯲'),int('🯳🯸'),int('-🯳🯵'),int('🯳🯴'),int('🯱🯲'),int('🯱🯶'),int('🯱🯴'),int('🯲🯷'),int('🯱🯲'),int('🯱🯷'),int('-🯳🯵'),int('🯱🯲'),int('🯳🯳'),int('🯲🯱'),int('-🯳🯲'),int('🯱🯲'),int('🯳🯲'),int('🯳🯳'),int('🯳🯴'),int('🯲🯹'),int('🯲🯲'),int('🯱🯷'),int('-🯳🯲'),int('🯳🯲'),int('🯳🯳'),int('🯱🯲'),int('🯳🯲'),int('🯳🯳'),int('🯳🯴'),int('🯱🯹'),int('🯱🯹'),int('🯴🯲')]

answer=input("Flag> ")

if len(𝓪𝓃𝘴𝔀𝓮𝓻)!=int('᧗')*int('߈')-int('𑄹'):
    print("Incorrect")
    quit()

for 𝙛𝙤𝙧 in range(len(𝘢𝘯𝓈𝘸𝘦𝘳)):
    if 𝒾𝒻[𝙛𝙤𝙧]!=ord(𝒶𝓷𝓼𝓌𝑒𝓇[𝙛𝙤𝙧])-eval("\U00000069\U0000006E\U00000074\U00000028\U00000027\U0000A9F9\U00000027\U00000029\U0000002A\U00000069\U0000006E\U00000074\U00000028\U00000027\U00000B6E\U00000027\U00000029\U0000002B\U00000069\U0000006E\U00000074\U00000028\U00000027\U00000A6A\U00000027\U00000029\U0000002B\U00000069\U0000006E\U00000074\U00000028\U00000027\U000009ED\U00000027\U00000029"):
        print("Incorrect")
        quit()

print("Success!")
```

In order to make the `if` array readable, I attempted to copy and paste it into a `python3` terminal and print it out. However, I got an error:

```
$ python3
Python 3.9.9 (main, Nov 16 2021, 10:24:31) 
[GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> test = [int('🯱🯶'),int('🯳🯳'),int('🯱🯹'),int('🯴🯰'),int('🯲🯲'),int('🯱🯲'),int('🯲🯵'),int('-🯳🯵'),int('🯳🯵'),int('🯱🯸'),int('🯱🯲'),int('🯳🯴'),int('🯲🯷'),int('🯲🯲'),int('🯱🯶'),int('-🯳🯵'),int('🯱🯷'),int('-🯳🯲'),int('🯱🯲'),int('🯱🯵'),int('��🯶'),int('🯱🯲'),int('🯳🯸'),int('-🯳🯵'),int('🯳🯴'),int('🯱🯲'),int('🯱🯶'),int('🯱🯴'),int('🯲🯷'),int('🯱🯲'),int('🯱🯷'),int('-🯳🯵'),int('🯱🯲'),int('🯳🯳'),int('🯲🯱'),int('-🯳🯲'),int('🯱🯲'),int('🯳🯲'),int('🯳🯳'),int('🯳🯴'),int('🯲🯹'),int('🯲🯲'),int('🯱🯷'),int('-🯳🯲'),int('🯳🯲'),int('🯳🯳'),int('🯱🯲'),int('🯳🯲'),int('🯳🯳'),int('🯳🯴'),int('🯱🯹'),int('🯱🯹'),int('🯴🯲')]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '��🯶'
>>>
```

Instead, I simply added in the line `print(𝒾𝒻)` after the array was initialized, which then printed out the array

```
[16, 33, 19, 40, 22, 12, 25, -35, 35, 18, 12, 34, 27, 22, 16, -35, 17, -32, 12, 15, 16, 12, 38, -35, 34, 12, 16, 14, 27, 12, 17, -35, 12, 33, 21, -32, 12, 32, 33, 34, 29, 22, 17, -32, 32, 33, 12, 32, 33, 34, 19, 19, 42]
```

In addition, I used the Find and Replace function in VS Code to change the variable `𝒾𝒻` to `var1` and `𝙛𝙤𝙧` to `i`. Also, I had to manually change all the variations of `answer` to the normal ASCII version for readability purposes. This resulted in the following code, which is much better, but not quite done:

```python
import base64

var1 = [16, 33, 19, 40, 22, 12, 25, -35, 35, 18, 12, 34, 27, 22, 16, -35, 17, -32, 12, 15, 16, 12, 38, -35, 34, 12, 16, 14, 27, 12, 17, -35, 12, 33, 21, -32, 12, 32, 33, 34, 29, 22, 17, -32, 32, 33, 12, 32, 33, 34, 19, 19, 42]

answer = input("Flag> ")

if len(answer) != int('᧗')*int('߈')-int('𑄹'):
    print("Incorrect")
    quit()

for i in range(len(answer)):
    if var1[i] != ord(answer[i]) - eval("\U00000069\U0000006E\U00000074\U00000028\U00000027\U0000A9F9\U00000027\U00000029\U0000002A\U00000069\U0000006E\U00000074\U00000028\U00000027\U00000B6E\U00000027\U00000029\U0000002B\U00000069\U0000006E\U00000074\U00000028\U00000027\U00000A6A\U00000027\U00000029\U0000002B\U00000069\U0000006E\U00000074\U00000028\U00000027\U000009ED\U00000027\U00000029"):
        print("Incorrect")
        quit()

print("Success!")
```

Using a python3 terminal, the line `int('᧗')*int('߈')-int('𑄹')` resulted in `53`, and the Unicode-encoded string (the `"\U00000069..."` line) resulted in `"int('꧹')*int('୮')+int('੪')+int('৭')"`. `int('꧹')*int('୮')+int('੪')+int('৭')` was then run and resulted in `83`. At this point, our unobfuscated script looks like this:

```python
import base64

var1 = [16, 33, 19, 40, 22, 12, 25, -35, 35, 18, 12, 34, 27, 22, 16, -35, 17, -32, 12, 15, 16, 12, 38, -35, 34, 12, 16, 14, 27, 12, 17, -35, 12, 33, 21, -32, 12, 32, 33, 34, 29, 22, 17, -32, 32, 33, 12, 32, 33, 34, 19, 19, 42]

answer = input("Flag> ")

if len(answer) != 53:
    print("Incorrect")
    quit()

for i in range(len(answer)):
    if var1[i] != ord(answer[i]) - 83:
        print("Incorrect")
        quit()

print("Success!")
```

It is now clear that the flag is 53 characters long, and the script takes the decimal value of the character, subtracts 83 from it, and see if it matches the corresponding element in the `var1` array. To get the flag, all we need to do is add 83 to every number in the array and convert to ascii. Using this code snippet will do so:

```python
for i in [16, 33, 19, 40, 22, 12, 25, -35, 35, 18, 12, 34, 27, 22, 16, -35, 17, -32, 12, 15, 16, 12, 38, -35, 34, 12, 16, 14, 27, 12, 17, -35, 12, 33, 21, -32, 12, 32, 33, 34, 29, 22, 17, -32, 32, 33, 12, 32, 33, 34, 19, 19, 42]:
    print(chr(i+83), end='')
```

**Flag** - `ctf{i_l0ve_unic0d3_bc_y0u_can_d0_th3_stupid3st_stuff}`