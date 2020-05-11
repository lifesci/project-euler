def find_cycle_len(x):
    num = 1
    den = x
    result = []
    indices = {}
    while True:
        if num == 0:
            return 1
        while num < den:
            num *= 10
        pair = (num, den)
        if pair in indices:
            index = indices[pair]
            break
        result.append(num//den)
        indices[pair] = len(result) - 1
        num = num % den
    return len(result) - index


max_len = -1
max_ind = -1
for i in range(1, 1000):
    cycle_len = find_cycle_len(i)
    if cycle_len > max_len:
        max_len = cycle_len
        max_ind = i
print(max_ind)
