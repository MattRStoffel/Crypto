#/usr/bin/python3
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

def miller_rabin_test(test_number, rounds_of_testing = 100):
    # Output: “composite” if n is found to be composite, “probably prime” otherwise
    d = 0
    s = test_number - 1

    # d odd > 0 such that n − 1 = 2sd  # by factoring out powers of 2 from n − 1
    while s % 2 == 0:
        s //= 2
        d += 1

    for _ in range(rounds_of_testing):
        a = random.randrange(2, test_number - 2)
        x = pow(a, s, test_number)
        if x == 1 or x == (test_number - 1): continue  # nontrivial square root of 1 modulo n
        for _ in range(d - 1):
            x = pow(x, 2, test_number)
            if x == test_number - 1: return False # nontrivial square root of 1 modulo n
        if not x == 1:
            return False
    return True

def randomPrime(accuracy = 40, size= 1024, p = False):
    if p:
        print("Generating a prime number of 2 ^", size)
    size = 2 ** size
    x = random.randrange(size / 2, size - 1)
    while(not miller_rabin_test(x, accuracy)):
        x = random.randrange(size / 2, size - 1)
    if p:
        print("The number is: \n", x)
    return x
