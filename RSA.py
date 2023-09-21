#/usr/bin/python3
import PrimeNumber as prime
import math

def generate_key_pair(key_size = 512):

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

    # Choose an integer e such that 2 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime.
    # for i in range(lam, 2):
    e = 65537
    
    # Determine d as d ≡ e−1 (mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n)
    d = pow(e, -1, lam)

    private_key = (d, n)
    public_key = (e, n)

    return private_key, public_key

def encription(message, public_key):
    message_ascii = int.from_bytes(message.encode('utf-8'), byteorder='big')
    ciphertext = pow(int(message_ascii), public_key[0], public_key[1])
    return ciphertext

def decryption(ciphertext, private_key, public_key):
    message_ascii = pow(ciphertext, private_key[0], private_key[1])
    message_bytes = message_ascii.to_bytes((message_ascii.bit_length() + 7) // 8, byteorder='big')
    return message_bytes.decode('utf-8')

def test(message):
    keys = generate_key_pair(key_size=64)
    ciphertext = encription(message, keys[1])
    message_out = decryption(ciphertext, keys[0], keys[1])
    print(message_out)
