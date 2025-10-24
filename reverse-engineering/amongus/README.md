# ඞ
Description:
```markdown
I feel like everyone thinks that interpreted rev is significantly easier than compiled rev. I also think all those oBfUsCaTeD jAvAsCriPt pAyLoAdS people find and reverse in the real world are made by ඞ amateurs. Let me know what you think.

https://amongus.youcanhack.me
```

## Writeup
The idea behind this challenge is to mimic real-world JavaScript reversing. Real-world JS reversing is oftentimes some fake login page or website that captures credentials and exfils it to an endpoint or other server, and a SOC analyst wants to know where it's going/what it's doing. Given this situation to emulate, it somewhat ties my hands and restricts how creative I can be, but I decided to make this "fake login page" target a specific individual. If the username matches, then the password is base64-encoded and XORed with the flag and sent to the `/exfil` endpoint using `fetch()`. Knowing this makes the solve trivial; determing this is anything but.

To obfuscate the code, I used a number of different tricks:
- All unnecessary whitespace was removed so everything is on the same line
- The [JSF**k](https://jsfuck.com/) library was used to obfuscate strings and a few lines of code
- Unicode codepoints 917760-917999 are invisible characters. While it's not a valid variable name alone, it can be paired with another character and only the other character is visible. In modern text editors like VSCode, this invisible character is recognized and the variable name is highlighted in yellow stating something along the lines of "there's an invisible character after this `a` in the variable name" so that developers don't get tricked. HOWEVER, if I use the Unicode amongus character `ඞ` instead of something like `a`, VSCode does *not* give this warning! Therefore, all variables (and object properties) are `ඞ` characters with different invisible characters afterwards. To get around that, you'll have to Find+Replace with regular variable names.
- If "bad behavior" is detected, the JS will replace with window with the YouTube short https://www.youtube.com/shorts/SknGKTTAZi0 (I apologize in advance). This includes using an incorrect username, trying to run a custom function in the browser after trying something with the correct username, etc. I almost went with hash checks of the actual code but decided to not.
- The username it looks for is `hackerschallenge2025_usernamehackerschallenge2025_username` and the password has to be at least 34 characters long. While the flag is actually 48 characters long, base64 encoding any 34-character string will result in a 48-character string.
- The flag (used as the XOR key) is generated based on the SHA256 hash of the username, so removing or skipping the username check will make the XOR key wrong and will lead to a confused participant.
- Hashing in JavaScript browser windows is always asynchronous, which makes it difficult to use. After some investigation, I found that [someone made a synchronous version online](https://github.com/6502/sha256/blob/main/sha256.js), but because JavaScript is asynchronous by nature, this sometimes leads to incorrect hashes. When ran in the code I provided, taking the "hash" of an input will give **incorrect but predictable results**. However, if you use the same function with the same input in the browser console, it will give correct results, thereby ALSO leading to a very confused participant. Thanks JavaScript.

**Flag** - `HC{I_h4t3_j4v3rscr1mpt_s00000_much_f3f1268182a0}`