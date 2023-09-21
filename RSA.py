import PrimeNumber as prime
import math

key_size = 2

# Choose two large prime numbers p and q.
p = prime.randomPrime(size=key_size)
q = prime.randomPrime(size=key_size)

# Compute n = pq.
n = p * q

# Compute λ(n), where λ is Carmichael's totient function. 
# Since n = pq, λ(n) = lcm(λ(p), λ(q))
# since p and q are prime, λ(p) = φ(p) = p − 1, and 
# likewise λ(q) = q − 1. Hence λ(n) = lcm(p − 1, q − 1).
lam = math.lcm(p - 1, q -1)

print(p, " ", q, " ", n, " ", lam)

# Choose an integer e such that 2 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime.
# for i in range(lam, 2):
