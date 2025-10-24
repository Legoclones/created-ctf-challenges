#!/usr/local/bin/python3

import hashlib

str1 = input("String 1: ")
str2 = input("String 2: ")

# ensure they're not the same
if str1 == str2:
    print("Strings must be different!")
    exit(1)

# ensure both start with the prefix
if not str1.startswith("hackerschallenge ") or not str2.startswith("hackerschallenge "):
    print("Strings must start with 'hackerschallenge '!")
    exit(1)

# ensure the first 5 bytes and last 4 bytes are the same
hash1 = hashlib.sha256(str1.encode()).hexdigest()
hash2 = hashlib.sha256(str2.encode()).hexdigest()

if (hash1[:5*2] != hash2[:5*2]) or (hash1[-4*2:] != hash2[-4*2:]):
    print("Hashes do not match!")
    exit(1)

# otherwise, give them the flag
print("Success! Here is your flag:")
print(open("flag.txt").read().strip())