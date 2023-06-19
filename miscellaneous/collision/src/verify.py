import base64
import hashlib

# get 2 base64-encoded strings from user (will only accept strings of length <= 10000)
str1 = input("Enter string 1: ")[:10000]
str2 = input("Enter string 2: ")[:10000]

# decode strings
pic1 = base64.b64decode(str1)
pic2 = base64.b64decode(str2)

# verify that both pictures are valid PNGs
if pic1[:8] != b'\x89PNG\r\n\x1a\n' or pic2[:8] != b'\x89PNG\r\n\x1a\n':
    print("Invalid PNG")
    quit()

# verify that both pictures have the same MD5 sum
if hashlib.md5(pic1).digest() != hashlib.md5(pic2).digest():
    print("MD5 sums do not match")
    quit()

# verify that base_str_1 is in one picture, and base_str_2 is in the other
base_str_1 = "Keeping your software and systems up-to-date with the latest security patches is a crucial step in safeguarding against potential cyber attacks."
base_str_2 = "Implementing strong passwords, two-factor authentication, and regular employee training are essential measures in maintaining a secure digital environment for your organization."

if (base_str_1.encode() in pic1 and base_str_2.encode() in pic2) or (base_str_2.encode() in pic1 and base_str_1.encode() in pic2):
    print("Strings found")
    print(open("flag.txt").read())
else:
    print("Strings not found")
