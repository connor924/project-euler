"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
 believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""
import math
from functools import reduce
import time
import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

start_time = time.time()


def is_digit_cancelling_fraction(numerator, denominator):
    """
    Takes 2-digit numerator and denominator where they both share a common digit. numerator < denominator
    Returns True if by removing the common digit from both the fraction is still equal to original
    """
    if numerator % 10 == 0 and denominator % 10 ==0:
        return False
    quotient = numerator / denominator
    common_digit = None
    for c in str(numerator):
        if c in str(denominator):
            common_digit = c
    if common_digit == None:
        return False
    else:
        new_numerator = str(numerator).replace(common_digit,'')
        new_denominator = str(denominator).replace(common_digit,'')
        if new_numerator == '' or new_denominator == '' or new_denominator == '0':
            return False
        new_quotient = int(new_numerator)/int(new_denominator)
        return quotient == new_quotient


non_trivial_answers = []
for numerator in range(10, 100):
    for denominator in range(10, 100):
        if numerator < denominator:
            if is_digit_cancelling_fraction(numerator, denominator):
                non_trivial_answers.append([numerator,denominator])

# get product of these
product_numerator = prod([x[0] for x in non_trivial_answers])
product_denominator = prod([x[1] for x in non_trivial_answers])

gcd = math.gcd(product_numerator, product_denominator)

print("Answer = %s" % (product_denominator / gcd))

print("--- %s seconds ---" % (time.time() - start_time))
