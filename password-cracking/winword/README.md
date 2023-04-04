# Winword
**Level**: Extreme

**Points**: 650

**Author**: Justin Applegate

**Description**:
```markdown
A suspected terrorist cell sent an encrypted Word document, which we have recovered. Can you crack it for us?

Note - you might want to use a BIG wordlist...

[winword.docx]
```

## Writeup
The only way to solve this problem is by using the biggest wordlist you can find, the full [crackstation.txt](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm) wordlist. The password is `´´´´´´´´`, which is near the top of the wordlist. However, the password is likely not to be found anywhere else.

**Flag** - `ctf{its_imp0rt4nt_t0_l34rn_h0w_t0_decrypt_all_types_0f_fil3s}`