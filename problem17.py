"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is
in compliance with British usage.

"""

import time

start_time = time.time()


ones = {'1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
        }

ten_through_19 = {'10': 'ten',
                  '11': 'eleven',
                  '12': 'twelve',
                  '13': 'thirteen',
                  '14': 'fourteen',
                  '15': 'fifteen',
                  '16': 'sixteen',
                  '17': 'seventeen',
                  '18': 'eighteen',
                  '19': 'nineteen'}

tens = {'2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'}

hundred = 'hundred'
thousand = 'thousand'
ones_list = ones.values()
ten_to_19_list = ten_through_19.values()

letter_count = 0
# one through 19 shows up 10 times
letter_count = letter_count + 10 * (sum([len(x) for x in ones_list]) + sum([len(x) for x in ten_to_19_list]))

# each tens value shows up 100 times
letter_count = letter_count + 100 * sum([len(x) for x in tens.values()])

# add the count from the ones 80 more times
letter_count = letter_count + 80 * sum([len(x) for x in ones_list])


# 900 occurrences of hundred
letter_count = len(hundred) * 900 + letter_count

# 100 occurrences of each of the ones as in *three* hundred and forty-two
letter_count = letter_count + 100 * sum([len(x) for x in ones_list])

# 891 occurrences of and
letter_count = letter_count + 892 * len('and')

# one occurrence of thousand
letter_count = letter_count + len(thousand)

print("Answer =  %s" % letter_count)


print("--- %s seconds ---" % (time.time() - start_time))