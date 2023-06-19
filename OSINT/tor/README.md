# TOR
Level - Medium

Description:
```markdown
I've recently been getting into TOR and figuring out how that all works. I recently came across a TOR relay with the fingerprint 301612857BAB556E60BB035FF1C9C76688BFED4A. Can you figure out the OR address that was associated with it?

*Note - you do not need to download/use/access the TOR browser or website to solve this challenge*

Flag format - `byuctf{XX.XX.XX.XX:XXXXX}`
```

## Writeup
The [relay search on metrics.torproject.org](https://metrics.torproject.org/rs.html#details/301612857BAB556E60BB035FF1C9C76688BFED4A) for that fingerprint shows a node called "BridgeTest1", but no OR address associated with it. However, looking up the [same thing on Onionite.net](https://onionite.net/node/301612857BAB556E60BB035FF1C9C76688BFED4A) shows the OR address as a local address.

**Flag** - `byuctf{10.54.14.33:55253}`