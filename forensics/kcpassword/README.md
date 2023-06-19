# kcpassword
Level - Easy

Description:
```
I'm too lazy to log into my Mac each time, so I enabled auto-logon. It's okay though because I'm sure that Apple will protect my password sufficiently...

[kcpassword]
```

## Writeup
When enabling auto-logon on a Mac, the OS will take your password, XOR it with a static key, and store it in the `kcpassword` file. To decrypt, simply XOR it with the static key again (https://github.com/Heisenberk/decode-kcpassword/blob/master/decode-kcpassword.py).

**Flag** - `byuctf{wow_Macs_really_have_it_encrypted_with_a_static_key_lol}`