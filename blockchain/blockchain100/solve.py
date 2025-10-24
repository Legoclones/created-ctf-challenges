# see https://github.com/CyberGX/MerkleRootCalculator/blob/master/MerkleRootCalculator.py
import requests, hashlib, binascii


URL = 'https://blockstream.info/api/block/000000000000000000003ed4a37d0591dea75e1894aa55e21d85ce4525542620/txids'
txids = requests.get(URL).json()

print(f'Len before: {len(txids)}')
txids.remove('112f9873468fa1f4f0944269ece08c11a34ca064fd603fa7335e4c1a7ca3f943')
print(f'Len after: {len(txids)}')


def hashIt(firstTxHash, secondTxHash):
    unhex_reverse_first = binascii.unhexlify(firstTxHash)[::-1]
    unhex_reverse_second = binascii.unhexlify(secondTxHash)[::-1]

    concat_inputs = unhex_reverse_first+unhex_reverse_second
    first_hash_inputs = hashlib.sha256(concat_inputs).digest()
    final_hash_inputs = hashlib.sha256(first_hash_inputs).digest()
    return binascii.hexlify(final_hash_inputs[::-1])
 
def merkleCalculator(hashList):
    if len(hashList) == 1:
        return hashList[0]
    newHashList = []
    
    for i in range(0, len(hashList)-1, 2):
        newHashList.append(hashIt(hashList[i], hashList[i+1]))
    if len(hashList) % 2 == 1:
        newHashList.append(hashIt(hashList[-1], hashList[-1]))
    return merkleCalculator(newHashList)

print(f'Root hash: {merkleCalculator(txids)}')