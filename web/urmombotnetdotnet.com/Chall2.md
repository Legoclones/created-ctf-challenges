# urmombotnetdotnet.com 2
Description:
```markdown
During my databases class, my group and I decided we'd create a web app with the domain urmombotnetdotnet.com, and wrote the relevant code. At first glance, it looks pretty good! I'd say we were pretty thorough. But were we thorough enough??

Oh... we also forgot to make the front end :)

`byuctf.xyz:40010`

--------------------

What is flag 2? (see `byuctf{fakeflag2}` in source)

[urmombotnetdotnet.com.zip]
```

## Writeup
The endpoint `/api/tickets` does not check the length of the description, even though the schema has only allocated 2048 characters. If you try to submit a ticket with more than that, an error will be thrown and the flag on line 43 of `ticket_routes.py` will be revealed.

**Flag** - `byuctf{oof_remember_to_check_length_limit}`