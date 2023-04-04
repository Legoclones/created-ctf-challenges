# Personal
**Level**: Hard

**Points**: 500

**Author**: Justin Applegate

**Description**:
```markdown
This is the hash of [Astoria Villin](https://twitter.com/AstoriaVillin) - based on personal information, can you crack her password?

`6eb65bb5967877e0c79e94ba8ca2518186caf05d9218001f5d121762929a32cb`

The flag is in the format `ctf{password}`
```

## Writeup
Finding the password to this hash requires combing Astoria's (fake) social media account and pulling out key information. A custom wordlist should then be created using these key words, such as first name, last name, spouse's name, birthdate, pet name, etc. This wordlist should then be mangled using a rule that adds numbers/symbols before/after, either by hand or by using [CUPP](https://github.com/Mebus/cupp).

**Flag** - `ctf{Villin74}`