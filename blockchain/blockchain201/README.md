# Blockchain 201
Description:
```markdown
Here's a little bank program I wrote. Can you hack it?

https://blockchain201.youcanhack.me

[Blockchain201.sol]
```

## Writeup
This contract deals with large numbers and signedness. Withdrawing a negative amount is allowed since the argument datatype is signed (`int48`), so you can withdraw a large amount which will pass the checks and set your amount to what you want. There are also restrictions on the amounts you can deposit to point people towards the withdrawal functionality. 

The solution is automated in `solve.py`.

**Flag** - `HC{gr34test_h31st_of_th3_c3ntury}`

## Hosting
This challenge should be a Docker container that runs the blockchain infrastructure on port 1337. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
docker compose up -d --build blockchain201
```

To stop the challenge:
```bash
docker compose down
```