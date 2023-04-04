# Guessy
**Level**: Medium

**Points**: 359

**Author**: Justin Applegate

**Description**:
```markdown
How good are you at password cracking?

[forensics-flag2.zip]
```

## Writeup
This challenge consists of a password-protected ZIP file with no background given. Using a tool like John the Ripper will allow you to extract the hash from the ZIP file, and the password was `12345`. Using a list of the most common passwords will result in you finding the password. After unlocking the ZIP file, a photo with the flag on it is found.

**Flag** - `ctf{digital_forensics_is_my_favorite}`