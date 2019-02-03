"""

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

"""

import time
import math
start_time = time.time()

# there are 40 steps to be taken here: 20 right and 20 down. The only thing that is different is the sequence.
# We will simply count the number of combinations by 40 choose 20 (the remaining 20 will by default be the other
# direction.


def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))


print("Answer = %s" % choose(40, 20))

print("--- %s seconds ---" % (time.time() - start_time))
