# MD5
**Level**: Hard

**Points**: 489

**Author**: Justin Applegate

**Description**:
```markdown
Bobby really likes fruits. In fact, Bobby likes fruits so much that he's made his password 3 fruit names in a row!! Can you figure out his password?

`e23968e2f63c66616aa5f4fc1e9c45407717270a`

Flag format - `ctf{password}`
```

## Writeup
To solve this challenge, you're required to make a custom and comprehensive list of fruit names (comprehensive enough to include passion fruit). After being standardized (all lowercase, no spaces or symbols), you need to create a custom, concatenated list of all possible combinations of fruit names.

**Flag** - `ctf{blackberrygrapepassionfruit}`