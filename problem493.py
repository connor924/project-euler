"""
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""

import time

start_time = time.time()

"""
WORK
Expected value of pick 1 is 1

Expected value of pick 2 is (9/69) * 1 + (60/69) * 2

Expected value of pick 3 is (9/69)(8/68) * 1 + (60/69)(18/68) * 2 + (60/69)(42/68) * 3

Expected value of pick 4 is (9/69)(8/68)(7/67) * 1 + (60/69)(18/68)(17/67) * 2 + (60/69)(42/68)(27/67) * 3 + 
                                                                                 (60/69)(42/68)(16/67) * 4

"""

print("--- %s seconds ---" % (time.time() - start_time))
