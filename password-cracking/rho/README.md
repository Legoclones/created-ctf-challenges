# Rho
Description:
```markdown
Birthday attacks are pretty cool because they really cut down the time for hash collisions, but the drawback is they require so much memory!! Maybe I can use [Pollard's Rho method](https://www.cs.csi.cuny.edu/~zhangx/papers/P_2018_LISAT_Weber_Zhang.pdf) to [reduce that](https://x.com/David3141593/status/1648458205171953664)...

`nc rho.youcanhack.me 1337`

[server.py]
```

## Writeup
To straight brute force a 72-bit hash, you'll need to go through `2**n` possibilities where `n=72` (not possible). However, if a birthday attack is sufficient (just *any* two hashes that are the same), you have to go through `2**(n/2)` possibilities, but you also have to retain a lookup table of `2**(n/2) * hash_length bytes`. Rho's method reduces the memory required to be `O(1)` to make the lookup process feasible. A straight birthday attack could require up to 576 GB (`2**(72/2) * 9`) of memory, or 288 GB of memory on average, making it infeasible.

Calculating the following solution (using `solve.py`) with 10 threads on a 2.50 GHz CPU took 1h47m:
```
Found colliding trails! (503528 trails total)
sha256_trunc(b'hackerschallenge ee0eb07398fb2b278d') => 386c439a40342203ea
sha256_trunc(b'hackerschallenge 464800293e6db7918b') => 386c439a40342203ea

real    107m55.681s
user    1074m48.595s
sys     0m50.954s
```

**Flag** - `HC{h4sh_c0ll1s10ns_4r3_c00l_but_1ts_r34lly_4ll_just_4_bunch_0f_m4th}`

## Hosting
This challenge should be a Docker container that runs `server.py` on port 1337. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
docker compose up -d --build
```

To stop the challenge:
```bash
docker compose down
```