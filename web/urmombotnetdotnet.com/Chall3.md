# urmombotnetdotnet.com 3
Description:
```markdown
During my databases class, my group and I decided we'd create a web app with the domain urmombotnetdotnet.com, and wrote the relevant code. At first glance, it looks pretty good! I'd say we were pretty thorough. But were we thorough enough??

Oh... we also forgot to make the front end :)

`byuctf.xyz:40010`

--------------------

What is flag 3? (see `byuctf{fakeflag3}` in source)

[urmombotnetdotnet.com.zip]
```

## Writeup
The endpoint `/api/tickets/<ticketid>` does not check the length of new message string, even though the schema has only allocated 2048 characters. If you try to submit a message over 2048 chars (or multiple that are over that), an error will be thrown and the flag on line 81 of `ticket_routes.py` will be revealed.

**Flag** - `byuctf{let's_not_even_talk_about_the_newline_injection...}`