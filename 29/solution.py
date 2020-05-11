def count_distinct(a_list, b_list):
    distinct = set()
    for a in a_list:
        for b in b_list:
            distinct.add(a**b)
    return len(distinct)

print(count_distinct(range(2, 101), range(2, 101)))
