"""
A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.
Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number
a right truncatable Harshad number.

Also:
201/3=67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10**14.

"""
import math
import time
import numpy as np
import sympy


def is_harshad(num):
    digits = []
    num_str = str(num)
    for i in num_str:
        digits.append(int(i))
    digit_sum = sum(digits)
    return num % digit_sum == 0


def is_right_trunc_harshad(num):
    if is_harshad(num):
        digits = []
        num_str = str(num)
        for i in num_str:
            digits.append(int(i))
        for x in range(-1, -1 * len(num_str), -1):
            if not is_harshad(int(num_str[:x])):
                return False
        return True
    else:
        return False


def is_strong_harshad(num):
    if is_harshad(num):
        digits = []
        num_str = str(num)
        for i in num_str:
            digits.append(int(i))
        digit_sum = sum(digits)
        quotient = num / digit_sum
        if is_prime(quotient):
            return True
        else:
            return False
    else:
        return False


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


def is_strong_right_trunc_harshad_prime(p):
    if len(str(p)) > 1:
        trunc_p = int(str(p)[:-1])
        return is_strong_harshad(trunc_p) & is_right_trunc_harshad(trunc_p)
    else:
        return False

start_time = time.time()
primes_list = sympy.primerange(0, 10**4)
print('Primes Generated...')
strong_right_trunc_harshad_primes = []

for p in primes_list:
    if is_strong_right_trunc_harshad_prime(p):
        strong_right_trunc_harshad_primes.append(p)

print("Answer = %s" % sum(strong_right_trunc_harshad_primes))
print("--- %s seconds ---" % (time.time() - start_time))

