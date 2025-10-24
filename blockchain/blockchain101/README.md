# Blockchain 101
Description:
```markdown
I know you've heard of blockchain, but have you ever interfaced with it? Now's your lucky day to get a crash course! More details are attached.

https://blockchain101.youcanhack.me

[Blockchain101.sol] [instructions.txt]
```

## Writeup
The whole point of this challenge is just to have them be able to connect to the infrastructure and interact with a smart contract. It's a lot harder than it sounds, so I included some instructions for them laying out what to do. There are a number of libraries out there that can accomplish this task, some require more code to be written than others. [Foundpy](https://github.com/Wrth1/foundpy) is a pretty low-line-of-code solution for this, but I wrote mine in Python using the web3 library.

The solution is automated using `solve.py` (once the constants are replaced for the instance).

**Flag** - `HC{is_bl0ckchain_really_f0r_n00bs??}`

## Hosting
This challenge should be a Docker container that runs the blockchain infrastructure on port 1337. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
docker compose up -d --build blockchain101
```

To stop the challenge:
```bash
docker compose down
```