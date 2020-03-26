def adapt_permutation(permutation, index):
    adapted = []
    for digit in permutation:
        adapted_digit = digit if digit < index else digit + 1
        adapted.append(adapted_digit)
    return adapted

def gen_permutations(prev_permutations, num_digits):
    if num_digits == 1:
        return [[0]]
    
    permutations = []
    for i in range(num_digits):
        for prev in prev_permutations:
            permutation = [i]
            adapted = adapt_permutation(prev, i)
            permutation += adapted
            permutations.append(permutation)
    return permutations

def main():
    num_digits = int(input('Enter number of digits in final number: '))
    limit = int(input('Enter permutation to locate: '))
    cur_digits = 1
    prev = None
    while cur_digits <= num_digits:
        prev = gen_permutations(prev, cur_digits)
        cur_digits += 1
    print(''.join([str(i) for i in prev[limit - 1]]))

if __name__ == '__main__':
    main()
