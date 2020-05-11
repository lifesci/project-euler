import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def seq_len(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

max_len = -1
max_a = None
max_b = None
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        cur_len = seq_len(a, b)
        if cur_len > max_len:
            max_len = cur_len
            max_a = a
            max_b = b
print(max_a * max_b)
