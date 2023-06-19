# Legoclones 1
Level - Easy

Description:
```markdown
For some reason completely incomprehensible to mankind, you have become sworn enemies of one of the BYUCTF organizers, Legoclones. In your efforts to defeat him, you have decided to go back to the origins of Legoclones to learn more about him. This is what you know so far:

- He once claimed that he's been going by the moniker "Legoclones" for over a decade
- There was a website that he adopted and fostered for about 3 years, based on Star Wars lore, that has become quite large

Your goal now is to find this website that he claims as "his". 

*Notes from the organizer:*
* *The remaining 4 Legoclones-related OSINT challenges will open up after this one*
* *Doxxing Legoclones in real-life will not help you in any of these OSINT challenges. Stick to Legoclones and not his real-life counterpart*
* *Flag format - `byuctf{https://subdomain.domain.tld}`*
```

## Writeup
While searching "lego clones" on any search engine will yield numerous results, searching specifically for "legoclones" (no space) will yield more limited results, one of which is Clone Trooper Wikia. Searching "legoclones" along with Star Wars will make Clone Trooper Wiki pop up earlier in search results.

**Flags** - `byuctf{https://clone.wikia.com}`, `byuctf{https://clonetrooper.wikia.com}`, `byuctf{https://clonetrooper.fandom.com}`


# Legoclones 2
Level - Hard

Description:
```markdown
As you've been doing research on Clone Trooper Wikia, you came to a stark realization - Legoclones mentioned "adopting" the wiki, not "founding" it! If you can find the username of the person who **originally** founded the wiki, perhaps you could convince them to get into a custody battle over the site and steal it away from Legoclones. Who originally founded Clone Trooper Wikia?

*Notes from the organizer:*
* *Doxxing Legoclones in real-life will not help you in any of these OSINT challenges. Stick to Legoclones and not his real-life counterpart*
* *Flag format - `byuctf{Username}`*
```

## Writeup
As far as I can tell, there are only 3 places in the entire publicly-available Internet where the founder of the Wiki is mentioned - [a personal history of the 617th Battalion written by Blyndblitz](https://clonetrooper.fandom.com/wiki/User:Blyndblitz/617th_History), [a site history recorded on Star Wars Fans Wiki](https://starwarsfans.fandom.com/wiki/Clone_Trooper_Wiki), and [this long message thread](https://clonetrooper.fandom.com/f/p/2165493779661016993/r/2165577858679000085) (like 40 messages down).

**Flags** - `byuctf{Anomanzor}`, `byuctf{Anonmazor}` (technically `Anonmazor` is incorrect as it was a mispelling of the name by Blyndblitz, but I'll count it anyway)


# Legoclones 3
Level - Hard

Description:
```markdown
Wow, this wiki is so old, it wasn't even captured by the Wayback Machine until a few years after it had started to flourish. Can you figure out the exact date and time the wiki was created? There may be somewhat reputable sources with a date listed, but in an effort to force you to find an authoritative, reputable source, I'm also requiring you to find the time it was created too. Because I'm too lazy to worry about timezones, the flag is only the minute of when it was created. 

For example, if you found the wiki was created at 01:23, then the flag is `byuctf{23}`.

*Notes from the organizer:*
* *Doxxing Legoclones in real-life will not help you in any of these OSINT challenges. Stick to Legoclones and not his real-life counterpart*
* *Flag format - `byuctf{00}`*
```

## Writeup
You can find the date in the [Star Wars Fans Wiki history](https://starwarsfans.fandom.com/wiki/Clone_Trooper_Wiki) (where the founder is also mentioned), but no time is listed (plus can you really trust it?). Instead, the intended solution is to go to https://clonetrooper.fandom.com/wiki/Clone_Trooper_Wiki?action=info, where it shows the exact date and time the site was created - `11:20`.

**Flag** - `byuctf{20}`

# Legoclones 4
Level - Medium

Description:
```markdown
Back in the day, Wikia allowed each person to put some data in their profile such as where you live and your current occupation. I only ever had 3 occupations listed in my profile at different times. What was one of them?

*Notes from the organizer:*
* *Doxxing Legoclones in real-life will not help you in any of these OSINT challenges. Stick to Legoclones and not his real-life counterpart*
* *Flag format - `byuctf{Exact text for occupation}`*
```

## Writeup
All of this information is found through the Wayback Machine (hinted in the previous chall) as it's not recorded in edit history. It's also wikia-wide, meaning it's the same on every single Wikia you could visit.

- AFJROTC Cadet (https://web.archive.org/web/20151103190612/http://clonetrooper.wikia.com/wiki/Message_Wall:Legoclones)
- Editing Clone Trooper Wiki (my website) (https://web.archive.org/web/20130524050235/http://clonetrooper.wikia.com/wiki/Message_Wall:Legoclones)
- Editing this wiki (https://web.archive.org/web/20120707154640/http://clonewars.wikia.com:80/wiki/User:Legoclones)

**Flags** - `byuctf{AFJROTC Cadet}`, `byuctf{Editing Clone Trooper Wiki (my website)}`, `byuctf{Editing this wiki}`, `byuctf{Editing Clone Trooper Wiki}`

# Legoclones 5
Level - Medium

Description:
```markdown
Since I was fairly young, I was still new to OPSEC and made a mistake - I posted my actual height for a short period before taking it down. Can you find it? 

The flag will be the day of the month that I posted my height. For example, if it was January 2nd, the flag would be `byuctf{02}`.

*Notes from the organizer:*
* *Doxxing Legoclones in real-life will not help you in any of these OSINT challenges. Stick to Legoclones and not his real-life counterpart*
* *Flag format - `byuctf{00}`*
```

## Writeup
I accidentally leaked my height on my profile on January 22nd, 2013 (https://clonetrooper.fandom.com/wiki/User:Legoclones?diff=8871&oldid=8858). I haven't really grown much since then either...

**Flags** - `byuctf{22}`