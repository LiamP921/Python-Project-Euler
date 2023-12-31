""" finds largest prime factor of 'n' """
def largest_prime_factor(n):
    i = 2
    while i * i < n:
        if n % i == 0:
            n //= i
        i += 1
    return n

print(largest_prime_factor(600851475143))
