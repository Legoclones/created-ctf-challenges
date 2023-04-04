# Library
Level - Easy

Description:
```
How many external library files does this `gpg` executable rely on?

Flag format - `byuctf{00}`

[gpg]
```

## Writeup
Running `ldd gpg | wc -l` gives you 14. The `ldd` command shows you exactly which libraries are needed for a binary to successfully run.

**Flag** - `byuctf{14}`
