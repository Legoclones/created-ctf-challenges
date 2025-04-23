# enr
Description:
```markdown
I just moved into a new apartment that came prefurnished with a Vilo router. To set up the router, I downloaded Vilo's app from the App Store and connected to my router. However, I'm a naturally curious person so I wanted to see what data my app was sending the router, and figured out how to capture traffic going to the router. Unfortunately, it seems some messages are encrypted, so I'm hoping the APK file will shed some light on this.

What's the non-null `enr` value being sent to the router?

Flag format - `byuctf{enrvalue}`

[enr.apk] [enr.pcapng]
```

## Writeup
This app uses BTEA and XXTEA to encrypt JSON messages using a randomly-generated key sent by the router in the 2nd message of each TCP stream. It also applies some custom deobfuscation functions to the values. Python does have an `xxtea` library, but we also pulled out the custom BTEA implementation they use as a Java file and have our solve script call it. The decryption process is scripted in `solve.py` and `pain.java`.

**Flag** - `byuctf{IQY6coUvUBQ8NOHw}`