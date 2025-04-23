# Musles
Description:
```markdown
Here's another binary to test your rev musles!! Let's see how you do :)

[musles]
```

## Writeup
This is a binary that uses musl instead of libc. It creates a new section of memory, writes encrypted shellcode to it, XORs it with a constant, and then runs the shellcode that will read in a flag and compare it to the correct flag.

**Flag** - `byuctf{ur_GDB_skills_are_really_swoll}`