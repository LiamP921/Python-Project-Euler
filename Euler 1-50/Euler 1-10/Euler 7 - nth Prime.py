from math import isqrt
import numpy as np

def sieveOfEratosthenes(limit):
    if limit < 2:
        return

    """ represents the number of odds <= 'limit'. """
    size = (limit - 1) // 2
    """ 'np.ones()' returns a new array of the given shape and data type, with values of '1'; acts as a primality tracker. """
    prime = np.ones(size + 1, dtype=bool)

    """ '.isqrt()' gets the integer square root of the given non-negative integer 'n'. It returns the floor value of the exact sqrt 
    of 'n', or equivalently the greatest integer 'a' such that 'a^2 <= n'. """
    for i in range(1, isqrt(limit) // 2 + 1):
        if prime[i]:
            p = i * 2 + 1
            """ updates all elements of 'prime' that correspond to multiples of the current prime 'p'. """
            prime[i + p::p] = False

    """ '.concatenate()' joins two or more arrays along a specified axis; '.nonzero()' computes the indices of non-zero elements, 
    returning a tuple of arrays, one for each dimension, containing said indices that dimension."""
    primes = np.concatenate(([2], np.nonzero(prime)[0] * 2 + 1))    
    return primes

def nthPrime(n):
    primes = sieveOfEratosthenes(150000)
    if n > len(primes):
        return None
    return primes[n]

if __name__ == '__main__':
    print(nthPrime(10001))

""" time complexity: 'O(n log log n)' """
