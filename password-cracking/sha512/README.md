# SHA512
**Level**: Easy

**Points**: 292

**Author**: Justin Applegate

**Description**:
```markdown
We managed to get another password, and we believe it's located in the rockyou.txt list. Can you find the password?

`236F5D6EA7C7A931B2D9C3D795F7EA1A6A943A62FCB141B02B5F016A98FA7A9BB305CA72FD880BA1BF9278DB0234FB063754BA560B9299B34A6DDCDF87F2039C`

The flag is in the format `ctf{password}`
```

## Writeup
Using [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) as the wordlist will result in the password being found.

**Flag** - `ctf{me160879ro}`