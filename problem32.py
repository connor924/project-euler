"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product
is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

"""
import time

start_time = time.time()

pandigital_products = set()


def has_pandigital_product_identity(i, j):
    pandigital_str = str(i) + str(j) + str(i*j)
    if len(pandigital_str) != 9:
        return False
    else:
        digit_set = ['1','2','3','4','5','6','7','8','9']
        for digit in digit_set:
            if digit not in pandigital_str:
                return False
        return True


for i in range(1, 10000):
    for j in range(1, 10000):
        if has_pandigital_product_identity(i, j):
            pandigital_products.add(i*j)


print("Answer = %s " % sum(pandigital_products))
print("--- %s seconds ---" % (time.time() - start_time))
