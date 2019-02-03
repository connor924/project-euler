"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


"""

import time

start_time = time.time()


def get_next_direction(dir):
    if dir == 'r':
        return 'd'
    if dir == 'd':
        return 'l'
    if dir == 'l':
        return 'u'
    if dir == 'u':
        return 'r'


def create_number_spiral(n):
    array = [[0 for x in range(n)] for y in range(n)]
    center = (int(n/2), int(n/2)) if n % 2 == 0 else (int((n-1)/2), int((n-1)/2))
    array[center[0]][center[1]] = 1
    num = 1
    step = 0
    phase = 0 # this increases distance every 2 turns
    distance = 1
    direction = 'r'
    current_cell = center
    # now we move in the next two directions with distance which increases every 2 turns
    while num < n**2:
        while step < distance:
            # First, we move each step in the distance in directions that alternate when distance is met
            if direction == 'r':
                num += 1
                current_cell = (current_cell[0], current_cell[1] + 1)
                array[current_cell[0]][current_cell[1]] = num
            elif direction == 'd':
                num += 1
                current_cell = (current_cell[0]+1, current_cell[1])
                array[current_cell[0]][current_cell[1]] = num
            elif direction == 'l':
                num += 1
                current_cell = (current_cell[0], current_cell[1]-1)
                array[current_cell[0]][current_cell[1]] = num
            elif direction == 'u':
                num += 1
                current_cell = (current_cell[0]-1, current_cell[1])
                array[current_cell[0]][current_cell[1]] = num

            step += 1
            if step == distance:
                direction = get_next_direction(direction)
            if num == n**2:
                break
        step = 0
        phase += 1
        if phase % 2 == 0:
            distance += 1

    return array


spiral_size = 1001
array = create_number_spiral(spiral_size)
print(array)

# count the diagonals
sum = 0
for i in range(0, spiral_size):
    sum += array[i][i]
    sum += array[i][spiral_size-1-i]
sum -= 1

print("Answer = %s" % sum)

print("--- %s seconds ---" % (time.time() - start_time))
