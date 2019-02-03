"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each
name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
 is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import os.path
import time
import string
start_time = time.time()
file = os.path.join('files', 'p022_names.txt')
name_list = []
for line in open(file):
    line = line.replace('"','')
    line = line.split(',')
    name_list = line

name_list.sort()


def get_name_score(index, name):
    score = [string.ascii_uppercase.index(x) for x in name]
    score = [int(x) + 1 for x in score]
    return sum(score) * (index+1)


score = 0
for index, name in enumerate(name_list):
    score = score + get_name_score(index, name)

print('Answer = %s' % score)


print("--- %s seconds ---" % (time.time() - start_time))
