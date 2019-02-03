
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

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


def get_digit_rotations(num):
    """
    returns list of all of the rotations of a number e.g. 197 will return [197, 971, 719]
    """
    rotations = [num]
    current_num = num
    for i in range(0, len(str(num))-1):
        current_num = str(current_num)[1:] + str(current_num)[0]
        rotations.append(int(current_num))
    return rotations


def is_circular_prime(num):
    if not is_prime(num):
        return False
    else:
        rotations = get_digit_rotations(num)
        for i in rotations:
            if not is_prime(i):
                return False
        return True


count = 0

for i in range(1,1000000):
    if is_circular_prime(i):
        count += 1

print("Answer = %s" % count)

print("--- %s seconds ---" % (time.time() - start_time))
