import math
import random

def primeSive(n):
    values = [True]*n
    for i in range(2,math.isqrt(len(values))+1):
        if(values[i]):
            x = i**2
            j = 1
            values[x] = False
            while (x + i * j) < len(values):
                values[x + i * j] = False
                j += 1
    return values
        
def generatePrimeList(n):
    primes = []
    for v, i in enumerate(primeSive(n)):
        if i:
            primes.append(v)
    return primes[2:]

def primeTest(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def randomPrime(minSize= 2**63, maxSize=2**64):
    x = -1
    while(not primeTest(x)):
        x = random.randrange(minSize, maxSize)
    return x

print(randomPrime())
