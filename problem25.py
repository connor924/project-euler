"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""
import time
start_time = time.time()


def return_next_fibonacci(f1, f2, fib_index):
    return f1 + f2, f2, fib_index


f_1 = 1
f_2 = 1
solved = False
index = 3
while not solved:
    next_fibonacci, prev_fibonacci, index = return_next_fibonacci(f_1, f_2, index)
    if len(str(next_fibonacci)) == 1000:
        solved = True
    else:
        f_1 = prev_fibonacci
        f_2 = next_fibonacci
        index = index + 1

print("Answer = %s" % index)

print("--- %s seconds ---" % (time.time() - start_time))
