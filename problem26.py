"""

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""
import time
start_time = time.time()


def get_length_of_recurring_cycle(d):
    """
    repeat the division algorithm until we find the length of the repeating segment
    """
    length = None
    viewed_chars = []
    current_char = 1 % d
    viewed_chars.append(current_char)
    end = False
    while not end:
        product = current_char * 10
        remainder = product % d
        if remainder in viewed_chars:
            length = len(viewed_chars) - viewed_chars.index(remainder)
            end = True
        elif remainder == 0:
            length = 0
            end = True
        else:
            current_char = remainder
            viewed_chars.append(current_char)
    return length


max_value = 0
max_length = 0

for i in range(2, 1001):
    length = get_length_of_recurring_cycle(i)
    if length > max_length:
        max_value = i
        max_length = length

print("Answer = %s with length %s" %(max_value, max_length))

print("--- %s seconds ---" % (time.time() - start_time))
