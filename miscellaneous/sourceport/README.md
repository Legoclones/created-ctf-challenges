# Source Port
Level: Easy

Description:
```
You can only get the flag if the source port of the connection is 42069. 

`nc byuctf.xyz 40002`
```

## Writeup
Use the command `nc byuctf.xyz 40002 -p 42069`.

**Flag** - `byuctf{l34rn1ng_t0_us3_n3tc4t_1s_v3ry_1mp0rt4nt}`

## Hosting
Simply run the Python script, and use `CTRL+C` to exit.