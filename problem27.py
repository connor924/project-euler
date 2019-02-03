"""
Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,
402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n=0.

"""
import time
import math
start_time = time.time()

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 1:
        for x in range(3, math.ceil(math.sqrt(num)+1), 2):
            if num % x == 0:
                return False
        return True
    else:
        return False

def consecutive_primes(a ,b):
    """
    returns number of consecutive primes for polynomial n^2 + an + b
    """
    count = 0
    prime = True
    n = 0
    while prime == True:
        if n**2 + a*n + b > 0:
            if is_prime(n**2 + a*n + b):
                count += 1
                n += 1
                prime = True
            else:
                prime = False
        else:
            prime = False
    return count


max = 0
max_a = 0
max_b = 0
for a in range(0, 1000):
    for b in range(0, 1001):
        candidate = consecutive_primes(a,b)
        if candidate > max:
            max = candidate
            max_a = a
            max_b = b
        candidate = consecutive_primes(-1 *a, b)
        if candidate > max:
            max = candidate
            max_a = -1 * a
            max_b = b
        candidate = consecutive_primes(-1 * a, -1 * b)
        if candidate > max:
            max = candidate
            max_a = -1 * a
            max_b = -1 * b
        candidate = consecutive_primes(a, -1 * b)
        if candidate > max:
            max = candidate
            max_a = a
            max_b = -1 * b

print("Answer = %s with length %s" %(max_a * max_b, max))

print("--- %s seconds ---" % (time.time() - start_time))

