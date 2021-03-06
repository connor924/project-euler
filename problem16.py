"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

"""

import time

start_time = time.time()

answer = sum([int(x) for x in str(2**1000)])

print("Answer = %s" % answer)

print("--- %s seconds ---" % (time.time() - start_time))

