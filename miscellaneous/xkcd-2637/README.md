# xkcd 2637
Level - Medium

Description:
```
Saw this and just couldn't resist.

`nc byuctf.xyz 40014`
```

## Writeup
This entire problem is just based around writing a script to solve [xkcd 2637](https://xkcd.com/2637/) (see explanation for algorithm to solve [here](https://www.explainxkcd.com/wiki/index.php/2637:_Roman_Numerals)).

The file `chall.py` is used to run the challenge, giving the flag after solving 500 problems. The script `solve.py` automatically solves it.

**Flag** - `byuctf{just_over_here_testing_your_programming_skills_:)}`

## Hosting
This challenge should be a Docker container that runs `python3 chall.py` on port 40014. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t xkcd2637 .
sudo docker network create -d bridge xkcd2637
```

The command to start the challenge is:

```bash
sudo docker run -p 40014:40000 --detach --name xkcd2637 --network xkcd2637 xkcd2637:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop xkcd2637
```