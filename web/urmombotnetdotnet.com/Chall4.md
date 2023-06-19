# urmombotnetdotnet.com 4
Description:
```markdown
During my databases class, my group and I decided we'd create a web app with the domain urmombotnetdotnet.com, and wrote the relevant code. At first glance, it looks pretty good! I'd say we were pretty thorough. But were we thorough enough??

Oh... we also forgot to make the front end :)

`byuctf.xyz:40010`

--------------------

What is flag 4? (see `byuctf{fakeflag4}` in source)

[urmombotnetdotnet.com.zip]
```

## Writeup
The endpoint `/api/register` ensures that the length of the username is at least 4 characters, but the flag is given if you can sign in successfully with a username under 4 characters. This is possible because registering with a Unicode character like `\u0000` passes the Python check, but is ignored in the login query (either the DB doesn't save the unicode char, or ignores it, not sure). Therefore, registering with a name like `"\u0000\u0000\u0000a"` means you can login with the username `"a"` successfully, getting the flag.

**Flag** - `byuctf{I_used_unicode_to_make_a_username_under_4_chars_wbu?}`