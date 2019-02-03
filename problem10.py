"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import math


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


primes = [2]

for i in range(3, 2000000, 2):
    if is_prime(i):
        primes.append(i)

print("Sum of primes = %s" % sum(primes))

print(primes[-10:])