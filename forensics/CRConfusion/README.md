# CRConfusion
Level - Hard

Description:
```
I told my friend that I want to learn how CRC works, so he sent me these three files. Apparently, each line of the text file uses a modified CRC to calculate a checksum. He said that if I can find the hidden message, I'll truly understand CRC...

[crc1.txt] [crc2.txt] [crc3.txt]
```

## Writeup
Cyclic Redundancy Checks use a specific pattern to calculate a fixed-length checksum based on a polynomial. This polynomial has to be the same length as the actual checksum (aka, 8-bit checksum means 8-bit polynomial), and is represented as hex. What I did for the challenge was use the character codes for each letter of the flag as the polynomial, and then calculated the CRC of a random 32-bit string (using [ctf_chall.py](ctf_chall.py)). This was done 3 times with the same flag to ensure no ambiguity. 

To solve, all it takes is brute forcing the polynomial with printable characters (~95) for each letter, and determine which single value will lead to the correct checksum for that line on all 3 files. That polynomial, when converted to ASCII, gives a letter of the flag. This process is automated in [solve.py](solve.py).

**Flag** - `byuctf{cyclic_redundancy_checks_are_used_to_detect_errors_in_data_transmission}`