# MD5
**Level**: Easy

**Points**: 86

**Author**: Justin Applegate

**Description**:
```markdown
We recovered two hashes from a database, and we need you to get the passwords:

`EDBD0EFFAC3FCC98E725920A512881E0`

`67881381DBC68D4761230131AE0008F7`

The flag is in the format `ctf{password1_password2}`
```

## Writeup
These two passwords are in rockyou.txt, the most common wordlists, or can be searched by simply putting the hash into Google. Plug the hash and wordlist into John the Ripper, Hashcat, or another password cracking program.

**Flag** - `ctf{iloveyou_babygirl}`