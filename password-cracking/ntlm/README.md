# NTLM
**Level**: Easy

**Points**: 397

**Author**: Justin Applegate

**Description**:
```markdown
I dumped the SAM, SYSTEM, and SECURITY files from a Windows machine and retrieved this hash. A text document said the password is only 4 characters long. Can you crack it?

`35505F45B250AC730941E8FED9C6EF14`

The flag is in the format `ctf{password}`
```

## Writeup
This flag can be brute force by specifying no options in John the Ripper or the incremental option in Hashcat. In addition, a text file of all possible four letter characters could be created and passed in as a wordlist. 

**Flag** - `ctf{heyo}`