# Zip
Level - Hard

Description:
```
This should be really easy, right?

[zip.zip]
```

## Writeup
The file `flag.txt` was zipped into `zip.zip` with the password `password123`. After brute forcing the password, you'll get the file, which says "XOR extra field with abcd". If you extract the bytes of the extra field (`CD A1 CA AA 8B A4 D8 ED DF A5 CE ED C8 A2 D9 BF CE AE DF ED E8 9F E8`), convert from hex, and XOR with 0xabcd, [you'll get the text](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'abcd'%7D,'Standard',false)&input=Q0QgQTEgQ0EgQUEgOEIgQTQgRDggRUQgREYgQTUgQ0UgRUQgQzggQTIgRDkgQkYgQ0UgQUUgREYgRUQgRTggOUYgRTgg) `flag is the correct CRC`. While unzipping, you'll notice that it says the CRC is wrong. At this point, just copy the correct CRC and put it in as the flag (note - many versions of the flag will be accepted).

**Flag** - `byuctf{ad74b76d}`