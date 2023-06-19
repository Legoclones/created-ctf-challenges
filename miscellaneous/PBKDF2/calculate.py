import hashlib, string
from itertools import product

base_passwd = b'isnt-byuctf-one-of-your-most-favorite-ctfs-even-though-this-is-only-our-second-year-'

for i in range(10):
    print(i)
    for pos in product(string.printable[:62], repeat=i):
        sha_1 = hashlib.sha1()
        sha_1.update(base_passwd+''.join(list(pos)).encode())
        hash = sha_1.digest()

        if all((char < 128 and char > 0x1f) for char in hash):
            print("GOT IT - ", hash.decode('utf-8'),base_passwd+''.join(list(pos)).encode())
            quit()