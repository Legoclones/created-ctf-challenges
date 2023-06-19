# 2038
Level - Easy

Description:
```
I know you really want the flag, so I'll print it out for you, but only after January 1st, 2024 :)

`nc byuctf.xyz 40007`

[2038]
```

## Writeup
This problem imitates the [Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem), where signed 32-bit integers can only go up to January 19th, 2038. Any number larger than that will overflow, causing it to be a negative value, starting in 1901. The date January 1st, 2024 in seconds since January 1st, 1970 is 1704067200. If you put in a number less than that, it will tell you it's too soon and exit early. If you put in a number larger than that, it will process it accordingly. 

If you enter a number > 2147483647 and < 4294967296, it will overflow and allow you to choose a time before 1970, which means the `print_flag` function will be called.

**Flag** - `byuctf{year_2038_problem_ftw}`

## Hosting
`2038` was compiled with `gcc -o 2038 -fstack-protector 2038.c`.

This challenge should be a Docker container that runs the executable `2038` every time someone connects on port 40007. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t 2038_chal .
sudo docker network create -d bridge 2038_chal
```

The command to start the challenge is:

```bash
sudo docker run -p 40007:40000 --detach --name 2038_chal --network 2038_chal 2038_chal:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop 2038_chal
```