# Brid
**Level**: Medium

**Points**: 465

**Author**: Justin Applegate

**Description**:
```markdown
There is a hidden file located on [brid.byuctf.xyz](http://brid.byuctf.xyz/). Can you find it?

**Note** - you *are* permitted to use automated scanners on this subdomain/website
```

## Writeup
A page was placed at `/server` with the flag on it. Using an automated scanning tool like Dirb (which backwards is "brid") would show the page is up.

**Flag** - `ctf{sometimes_bruteforcing_actually_works}`