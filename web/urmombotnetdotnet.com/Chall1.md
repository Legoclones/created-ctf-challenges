# urmombotnetdotnet.com 1
Description:
```markdown
During my databases class, my group and I decided we'd create a web app with the domain urmombotnetdotnet.com, and wrote the relevant code. At first glance, it looks pretty good! I'd say we were pretty thorough. But were we thorough enough??

Oh... we also forgot to make the front end :)

`byuctf.xyz:40010`

--------------------

What is flag 1? (see `byuctf{fakeflag1}` in source)

[urmombotnetdotnet.com.zip]
```

## Writeup
The endpoint `/api/register` does many checks on the user-supplied input, however it never checks for a duplicate email or that the bitcoin wallet or email are under 255 characters. Since our database schema specifies a length limit and that emails must be unique, an error will be thrown and the flag on line 48 of `login_routes.py` will be revealed. 

**Flag** - `byuctf{did_you_stumble_upon_this_flag_by_accident_through_a_dup_email?}`