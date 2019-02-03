"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.



"""
import time
start_time = time.time()


def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n/i != 1:
                divisors.append(int(n/i))
    return divisors


def get_proper_divisors(n):
    proper_divisors = get_divisors(n)
    proper_divisors.remove(n)
    proper_divisors = list(set(proper_divisors))
    return proper_divisors


def is_abundant_number(n):
    """
    returns True for abundant numbers
    """
    if sum(get_proper_divisors(n)) > n:
        return True
    else:
        return False


limit = 28124
abundant_list = []
for i in range(2, limit):
    if is_abundant_number(i):
        abundant_list.append(i)

non_abundant = set(list(range(1, limit)))
for i in abundant_list:
    for j in abundant_list:
        if i + j in non_abundant:
            non_abundant.remove(i+j)

print("Answer = %s" % sum(non_abundant))

print("--- %s seconds ---" % (time.time() - start_time))
