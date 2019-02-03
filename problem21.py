"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
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


def sum_of_proper_divisors(n):
    proper_divisors = get_divisors(n)
    proper_divisors.remove(n)
    return sum(proper_divisors)


def has_amicable_partner(n):
    sum_of_d = sum_of_proper_divisors(n)
    if n == sum_of_proper_divisors(sum_of_d) and n != sum_of_d:
        return True
    else:
        return False

sum_of_amicable_numbers = 0
for i in range(2, 10000):
    if has_amicable_partner(i):
        print('%s is amicable' % i)
        sum_of_amicable_numbers = sum_of_amicable_numbers + i

print("Answer = %s" % sum_of_amicable_numbers)

print("--- %s seconds ---" % (time.time() - start_time))
