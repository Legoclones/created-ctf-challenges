# PNG
Level - Hard

Description:
```
Wait, why can't I see it? The data is all there, obviously...

[kali.png]
```

## Writeup
This screenshot of a Kali terminal with a flag planted on it had the [dimensions removed from the metadata](http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html), so parsers won't know how to show it. Therefore, brute forcing the dimensions (width, specifically) will allow you to discover how big it is and show the photo properly. 

The original dimensions are 1453 (0x5ad) by 1080 (0x438).

This is similar to [a problem in the US Cyber Open](https://github.com/tj-oconnor/cyber-open-2022/tree/main/forensics/zerozero2Hero), where you had to brute force dimensions either by 1) creating a photo with several possible widths, or 2) brute forcing the dimensions based on the CRC value. Either one works.

**Flag** - `byuctf{kn0wing_f1le_f0rmats_is_k3y}`