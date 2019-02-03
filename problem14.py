"""

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
import time

start_time = time.time()


def collatz_sequence(n, current_sequence=[]):
    current_sequence.append(int(n))
    if n % 2 == 0:
        return collatz_sequence((n/2), current_sequence)
    elif n == 1:
        return current_sequence
    else:
        return collatz_sequence(3 * n + 1, current_sequence)

current_st_number = 0
longest_chain = 0
for i in range(500000,1000000):
    candidate = collatz_sequence(i, [])
    candidate_size = len(candidate)
    if candidate_size > longest_chain:
        current_st_number = i
        longest_chain = candidate_size

print("Answer = %s with chain length of %s" % (current_st_number, longest_chain))
print("--- %s seconds ---" % (time.time() - start_time))
