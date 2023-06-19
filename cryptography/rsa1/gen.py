from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

bits = 512
p=getPrime(bits)
print ("\nRandom n-bit Prime (p): ",p)

q=getPrime(bits)
print ("\nRandom n-bit Prime (q): ",q)

N=p*q
print ("\nN=p*q=",N)

PHI=(p-1)*(q-1)
print ("\nPHI (p-1)(q-1)=",PHI)

e=65537
print ("\ne=",e)

M = bytes_to_long(b'byuctf{NEVER_USE_SAME_MODULUS_WITH_DIFFERENT_e_VALUES}')

print ("\n\n=== Let's try these keys ==")
print ("\nRSA Message: ",M)

enc=pow(M,e,N)
print ("RSA Cipher(c=M^e mod N): ",enc)