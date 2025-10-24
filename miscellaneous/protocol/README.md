# Protocol
Description:
```markdown
Reverse engineering blind remote protocols can suck.... but verbose logging can make all the difference!

*Note - all messages are newline-terminated*

`nc protocol.youcanhack.me 1337`
```

## Writeup
The goal is for the user to interact with a remote service that uses an unknown protocol. While it does require some brute forcing (people may call it "guessy"), the brute force will be limited and verbose error messages should make the "next step" fairly easy to determine.

The flag is split into two stages - the first is given if the message type is `0xc0`, the second is given if:
- Debug mode is enabled (sending the message with type `0xff` and length 0)
- A specific "debug message" is sent (which is returned to the user if the message is wrong)
- The correct MD5 hash of the debug message is sent afterwards

Note that all messages follow the TLV format with a single byte for type and 2 bytes (little endian) for the length of the payload, followed by the payload.

The solve is automated in `solve.py`.

**Flag** - `HC{bl1nd_pr0t0c0l_4n4lys1s_sucks_but_1s_necess4ry_s0met1m3s}`

## Hosting
This challenge should be a Docker container that runs `server.py` on port 1337. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
docker compose up -d --build
```

To stop the challenge:
```bash
docker compose down
```