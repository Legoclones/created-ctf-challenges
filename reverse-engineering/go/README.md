# Go
Level - Medium

Description:
```
This is the first Go binary I've ever written, so the logic shouldn't be too complex.

[go]
```

## Writeup
The premise for the binary is fairly simple - pass in the correct string that matches the MD5 hash `27443509682471009008637982892046`, and then it will be used as the seed for a random number generator. Then, generate 24 random numbers and XOR with a static binary array to get the flag. 

Go binaries are much different than C binaries, so decompilation can be hard. However, after getting the MD5 hash for the inputted string, changing it in GDB to the desired value will let it take the correct logic and print out the flag for you. 

To solve, put a breakpoint at `0x48fc7c`, and run the following gdb commands to set the MD5 hash to the correct one:

```
gef>  set {int} 0x0000c0001ac020 = 0x34343732
gef>  set {int} 0x0000c0001ac024 = 0x39303533
gef>  set {int} 0x0000c0001ac028 = 0x34323836
gef>  set {int} 0x0000c0001ac02c = 0x30303137
gef>  set {int} 0x0000c0001ac030 = 0x38303039
gef>  set {int} 0x0000c0001ac034 = 0x39373336
gef>  set {int} 0x0000c0001ac038 = 0x39383238
gef>  set {int} 0x0000c0001ac03c = 0x36343032
gef>  x/s 0x0000c0001ac020                              # to verify the hash is actually what you want it to be
0xc0001ac020:   "27443509682471009008637982892046"
gef>  continue
Continuing.
Flag: byuctf{wake_up_to_g0_g0}
```

**Flag** - `byuctf{wake_up_to_g0_g0}`

## Hosting
`go` binary was compiled with the command `go build go.go`.