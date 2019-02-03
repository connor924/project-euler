"""

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""
import time

start_time = time.time()


def check_sum_digit_fifth_powers(num):
    digits = [int(s) for s in str(num)]
    fifth_powers = [x**5 for x in digits]
    return sum(fifth_powers) == num


# 1 million is an upper bound because n grows faster than the sum of fifth power digits of n as you can see
# 6 * 9^5 = 354294 < 999999 . This will continue to be true considering all nines is the max fifth power digit sum.

numbers = []
for i in range(10, 1000000):
    if check_sum_digit_fifth_powers(i):
        numbers.append(i)


print(numbers)

print("Answer = %s" % sum(numbers))

print("--- %s seconds ---" % (time.time() - start_time))
