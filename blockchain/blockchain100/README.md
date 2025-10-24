# Blockchain 100
Description:
```markdown
Provide the root hash of Bitcoin block 905090 as if transaction 112f9873468fa1f4f0944269ece08c11a34ca064fd603fa7335e4c1a7ca3f943 never happened.

**Flag format** - `HC{0000000000000000000000000000000000000000000000000000000000000000}`
```

## Writeup
The root hash is the merkle root of all transaction hashes, and calculating it [is explained well here](https://developer.bitcoin.org/reference/block_chain.html#merkle-trees). My solve script embedded [this script](https://github.com/CyberGX/MerkleRootCalculator/blob/master/MerkleRootCalculator.py) in it. The merkle root is calculated so if any transaction is modified/removed/added, then the root hash changes and therefore the block itself changes, providing immutability to the chain.

The solve involves looking up block 905090 to find the block hash, retrieving all the transaction IDs, removing the identified one, then re-calculating the merkle root. See `solve.py`.

**Flag** - `HC{fdc9e268aa0fca66941a8a4f18175dd36a65bc88e1bf4eb9ed0e3c8c550a205c}`