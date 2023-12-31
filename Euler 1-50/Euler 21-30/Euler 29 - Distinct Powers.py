""" calculates the no. of distinct terms in the sequence generated by 'a^b' for 2 <= a <= n and 2 <= b <= n. """
from itertools import product

def distinctPowers(n):
    distinct_terms = set()
    """ 'product' computes the cartesian product of a variable, and the product of an iterable itself via the specified no. of repetitions; this is output as tuples in sorted order. """
    for a, b in product(range(2, n + 1), repeat = 2):
        next_term = a ** b
        distinct_terms.add(next_term)

    return len(distinct_terms)

print(distinctPowers(100))
