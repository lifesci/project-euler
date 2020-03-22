# To get from the top left corner to the bottom right corner of an nxn
# grid, exactly n down moves and n right moves must be performed. Hence
# the total number of ways that one make this traversal is equal to the
# total number of ways that n right moves can be interspersed between n
# down moves (or vice-versa). To calculate this, we can use binomial
# coefficients. So the answer for an nxn grid is 40 choose 20.

import math

def binomial_coef(n, k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n - k))

print(binomial_coef(40, 20))
