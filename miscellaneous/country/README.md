# Country
**Level**: Hard

**Points**: 454

**Author**: Justin Applegate

**Description**:
```markdown
Our antivirus detected a malicious file on our machine and has given us the hash:

`a259082f33573151375ea00df28468fd`

We'd like to know more information about it. 

-----------------

What country are the attackers likely from?

Flag format - `ctf{country}` (case insensitive)
```

## Writeup
There are multiple ways to tie the creator of the malware to a specific country. However, one way is through the domain identified in the previous problem. The domain, `ttgholidays.com`, is not accessible anymore. A simple Google search for the domain will reveal social media sites associated with this domain known as ["The Travel Guide Holidays"](https://www.facebook.com/ttgholidays/), located in Jaipur, Rajasthan, India. 

Although this organization may not actually be affiliated with the hackers, a photo from their website was used in a shell command issued. Malicious actors often use resources like these from known or familiar locations or organizations. 

![](solution.png)

**Flag** - `ctf{India}`