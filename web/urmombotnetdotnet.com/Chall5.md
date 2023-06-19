# urmombotnetdotnet.com 5
Description:
```markdown
During my databases class, my group and I decided we'd create a web app with the domain urmombotnetdotnet.com, and wrote the relevant code. At first glance, it looks pretty good! I'd say we were pretty thorough. But were we thorough enough??

Oh... we also forgot to make the front end :)

`byuctf.xyz:40010`

--------------------

What is flag 5? (see `byuctf{fakeflag5}` in source)

[urmombotnetdotnet.com.zip]
```

## Writeup
When a bot is added to the botnet database through the `/api/bots` endpoint, the IP address is put through `ipaddress.ip_address(ip_address)`. If any errors are thrown, it exits early. However, only 256 chars are allocated for this field. So, an IP address string with a length > 256 will throw an error. This may initially seem impossible, except IPv6 have a scope field that is an arbitrary string using the `%` delimiter. For example, the following IPv6 address is valid and will pass the check - `"2001:db8::1000%111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"`. Using this IP address will cause the flag on line 88 of `account_routes.py` to be revealed. 

**Flag** - `byuctf{IPv6_scopes_are_just_arbitrary_strings...maybe_there_are_more_vulns_worldwide?}`