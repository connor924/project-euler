"""

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import time
start_time = time.time()

total_permutations = 10*9*8*7*6*5*4*3*2*1
string = "0123456789"
digits = [x for x in string]

def find_next_permutation(digits):
    # first find the shifting character
    shift_char = ''
    shift_char_loc = None
    for i in range(0,len(digits)-1):
        if digits[i] < digits[i+1]:
            shift_char = digits[i]
            shift_char_loc = i
        elif i == len(digits)-2 and shift_char_loc is None:
            shift_char = digits[i+1]
            shift_char_loc = i+1
    # next find character to swap with
    swap_char = 'A'
    swap_char_loc = None
    for i in range(shift_char_loc+1, len(digits)):
        if digits[i] < swap_char and digits[i] > shift_char:
            swap_char = digits[i]
            swap_char_loc = i
    # switch these two characters
    digits[shift_char_loc] = swap_char
    digits[swap_char_loc] = shift_char
    # re-sort the list after the original index of the shift char
    stable_part = digits[:shift_char_loc+1]
    sorting_part = digits[shift_char_loc+1:]
    sorting_part.sort()
    return stable_part + sorting_part


count = 1
while count < 1000000:
    digits = find_next_permutation(digits)
    count = count + 1

print('Answer = %s' % digits)


print("--- %s seconds ---" % (time.time() - start_time))