"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import time

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


def is_left_truncatable_prime(n):
    num_digits = len(str(n))
    if num_digits == 1:
        return False
    for i in range(0, num_digits):
        new_num = int(str(n)[i:])
        print(new_num)
        if not is_prime(new_num):
            return False
    return True


def is_right_truncatable_prime(n):
    num_digits = len(str(n))
    if num_digits == 1:
        return False
    for i in range(0, num_digits):
        new_num = int(str(n)[0:num_digits - i])
        print(new_num)
        if not is_prime(new_num):
            return False
    return True

def return_all_left_and_right_truncatable_primes():
    """
    This begins with the numbers 2, 3, 5, 7 and appends to left and right until we have all of the L & R truncatable
    primes. We stop this loop when there are no new truncatable primes to create. e.g. if we have a 5 digit truncatable
    prime and there are no 6 digit truncatable primes then we know that there cannot be any new ones to create
    :return: list of all L & R truncatable primes
    """
    # These are all of the single digit prime numbers
    starting_digits = [2, 3, 5, 7]
    # These are the only possible digits we can add or else there will be non-prime when we truncate
    add_digits = [1, 3, 7, 9]
    results = []
    for prime in starting_digits:
        candidate = prime
        while candidate


print("--- %s seconds ---" % (time.time() - start_time))