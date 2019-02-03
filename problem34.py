"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""
import time
import math

start_time = time.time()


def is_curious_number(num):
    """
    returns true if the number is equal to the sum of the factorial of its digits
    """
    digits = [int(x) for x in str(num)]
    digits_factorial = list(map(math.factorial, digits))
    return sum(digits_factorial) == num


# first we need to find a boundary to test up to
# we can use 9! as a gauge of how fast the factorial sum grows.. we see that 7*9! = 2540160 and 8*9! = 2903040
# since these are both 7 digit numbers we see that at this point the factorial sum is growing slower than adding
# additional digits. Thus, we can use the 7 digit 2540160 as an upper bound

curious_numbers = []
for i in range(10, 2540161):
    if is_curious_number(i):
        curious_numbers.append(i)

print("Answer = %s" % sum(curious_numbers))

print("--- %s seconds ---" % (time.time() - start_time))
