"""

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""
import time
import math

start_time = time.time()


def convert_to_binary_string(num):
    """
    takes an number in base 10 and returns a string with the binary equivalent
    """
    return bin(num)[2:]


def is_palindromic(str):
    """
    returns true if the string is palindromic
    """
    return str == str[::-1]


limit = 1000000
answers = []
for i in range(1, limit, 2):  # only odd numbers can be palindromic in base 2
    if is_palindromic(str(i)) and is_palindromic(convert_to_binary_string(i)):
        answers.append(str(i))

print("Answer = %s" % sum(list(map(int, answers))))
print("--- %s seconds ---" % (time.time() - start_time))
