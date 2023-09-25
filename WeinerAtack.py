#!/user/bin/pthon3
import RSA

keys = RSA.key(16)

print("Both keys   n :", keys.n)
print("Private key d :", keys.d)
print("Public key  e :", keys.e)

