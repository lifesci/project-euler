def power_sum(n):
    target = n
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 5
        n = n // 10
    return total == target

all_nums = 0
for i in range(2, 1000000):
    p_sum = power_sum(i)
    if p_sum:
        all_nums += i
print(all_nums)
