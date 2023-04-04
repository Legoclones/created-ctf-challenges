# One Time Pad
Level: Medium

Description:
```
I just learned about an encryption algorithm that is impossible to break, so I will give you the ciphertext because I know that you can't break it. In fact, I'm so confident that you can't crack it that I'm willing to tell you I used my password as the secret key!

`SKWDHAICUG`

Flag format - `byuctf{ANENGLSHPHRSE}`
```

## Writeup
Using a list of common passwords to brute force the secret key will reveal that the password `qwertyuiop` gives a ciphertext `COSMOCOUGR`. 

**Flag** - `byuctf{COSMOCOUGR}`
