# Pwntools
Level - Medium

Description:
```
You're solving a binary exploitation (pwn) CTF problem with a Python script and the `pwntools` Python module. You can manually run the exploit in GDB, but are having trouble getting your script to do the same thing. You decide to use the built-in GDB debugging functionality of `pwntools`, but it's missing a dependency on your system. You've already installed GDB, what else do you need to install?

Flag format - `byuctf{programname}`
```

## Writeup
`gdbserver` needs to be installed.

**Flag** - `byuctf{gdbserver}`