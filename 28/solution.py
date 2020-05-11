def sum_diagonals(max_side_len):
    if max_side_len == 0:
        return 0
    total = 1
    cur_side_len = 3
    cur_num = 1
    while cur_side_len <= max_side_len:
        for _ in range(4):
            cur_num += cur_side_len - 1
            total += cur_num
        cur_side_len += 2
    return total

print(sum_diagonals(1001))
