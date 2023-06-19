# Ducky2
Level - Medium

Description:
```
Okay, turnsk out that wask too easy to decode. You skhoud definitely try thisk one now!

[inject.bin]
```

## Writeup
Using one of the tools available in the first won't work because this uses SK.json as the keyboard layout. The text is pretty readable (gives you `makesurezourkezboardissetupright`), but the symbols in the remainder of the flag won't decode right. You'll have to use the JSON file available [here](https://github.com/hak5/usbrubberducky-payloads/blob/master/languages/sk.json) to decode it.

**Flag** - `byuctf{makesureyourkeyboardissetupright)@&%(#@)!(#*$)}`