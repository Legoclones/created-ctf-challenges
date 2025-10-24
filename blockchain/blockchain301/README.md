# Blockchain 301
Description:
```markdown
Can you win the lottery 10 times in a row?

https://blockchain301-7944b7.youcanhack.me

[Blockchain301.sol]
```

## Writeup
In order to get the flag, the user has to win the lottery 10 times in a row. To win the lottery, they have to make a transaction with 1 wei that has a 32-byte `value` argument. This value must match the block hash number of `lotteries_won`. Therefore, in order to win, they have to submit the hash of block 0, then the hash of block 1, then the hash of block 2, etc. These can be retrieved easily, in my solve I used `w3.eth.get_block(block_num).hash`. Note that when the contract is initially deployed, there's only 1 block (block 0). However, whenever the `lottery()` function is run, a new block is created because a transaction has to be made to run the function. Therefore, the block created from running `lottery()` the first time is the hash for the second `lottery()` run.

The solution is automated in `solve.py`.

**Flag** - `HC{g0tta_l0ve_cha1n-bas3d_r4nd0m_numb3rs}`

## Hosting
This challenge should be a Docker container that runs the blockchain infrastructure on port 1337. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
docker compose up -d --build blockchain301
```

To stop the challenge:
```bash
docker compose down
```