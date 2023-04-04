# Composer 2
**Level**: Medium

**Points**: 500

**Author**: Justin Applegate

**Description**:
```markdown
What is the secret message?

Flag format - `ctf{putsecretmessagehere}`

[mySong.wav]
```

## Writeup
This challenge builds on the previous one, Composer. Using [virtualpiano.net's keyboard](https://virtualpiano.net/), characters can be turned into notes. The WAV file, at first inspection, seems to have a bunch of random notes at a regular beat. However, if each specific note is matched to the corresponding letter on the keyboard for virtualpiano.net, the flag is found.

**Flag** - `ctf{doyouknowhowtoplaymusicwithyourkeyboard}`