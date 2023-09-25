#/usr/bin/python3
import PrimeNumber as prime
import math

class key:
    pri: (int, int)
    pub: (int, int)
    p : int
    q : int
    n : int
    lam : int
    e : int
    d : int

    def __init__(self,key_size= 512, pri=0, pub=0):
        self.pri = pri
        self.pub = pub
        if pri == 0 and pub == 0:
            self.generate_key_pair(key_size)
    
    def generate_key_pair(self, key_size = 512):
        # Choose two large prime numbers p and q.
        self.p = prime.randomPrime(size=key_size)
        self.q = prime.randomPrime(size=key_size)

        # Compute n = pq.
        self.n = self.p * self.q

        # Compute λ(n), where λ is Carmichael's totient function. 
        # Since n = pq, λ(n) = lcm(λ(p), λ(q))
        # since p and q are prime, λ(p) = φ(p) = p − 1, and 
        # likewise λ(q) = q − 1. Hence λ(n) = lcm(p − 1, q − 1).
        self.lam = math.lcm(self.p - 1, self.q -1)

        # Choose an integer e such that 2 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime.
        self.e = 65537
        
        # Determine d as d ≡ e−1 (mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n)
        self.d = pow(self.e, -1, self.lam)

        self.pri = (self.d, self.n)
        self.pub = (self.e, self.n)

    def encription(self, message):
        message_ascii = int.from_bytes(message.encode('utf-8'), byteorder='big')
        ciphertext = pow(int(message_ascii), self.e, self.n)
        return ciphertext

    def decryption(self, ciphertext):
        message_ascii = pow(ciphertext, self.d, self.n)
        message_bytes = message_ascii.to_bytes((message_ascii.bit_length() + 7) // 8, byteorder='big')
        return message_bytes.decode('utf-8')

    def test(self, message):
        keys = self.generate_key_pair(key_size=64)
        ciphertext = self.encription(message)
        message_out = self.decryption(ciphertext)
        print(message)
        print(self.pri, self.pub)
        print(ciphertext)
        print(message_out)
