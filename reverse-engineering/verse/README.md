# Verse
Description:
```markdown
My favorite Fortnite creator said he made an unwinnable island, but some source code for the island accidentally got leaked... Can you help me be the first to beat it?

[verse.verse]
```

## Writeup
The non-obfuscated version can be found at `og.verse`. The setup for the island has 480 switch devices which essentially function as "bits". This code loops through all 480 switch devices and makes an array of booleans (called "logics") with `false` if the switch is not on and `true` if it is. Then, an array of tuples is looped through; each tuple has 2 digits, and these represent 2 bits that need to be exchanged with each other. For example, `[(1,2), (3,4)]` mean that bits 1 and 2 need to be exchanged, and 3 and 4 need to be exchanged. Then, another array contains what the array should look like after exchanging bits (but backwards).

The solve is automated in `solve.py`.

**Flag** - `byuctf{this_language_is_supposed_to_be_beginner-friendly???}`