import math

def is_abundant(num):
    factors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.add(i)
            if i != 1:
                factors.add(num//i)
    return sum(factors) > num

def main():
    abundant = []
    for i in range(1, 28124):
        if is_abundant(i):
            abundant.append(i)
    abundant.sort()
    all_abundant_sums = set()
    for i in range(len(abundant)):
        first = abundant[i]
        if first >= 28124:
            break
        for j in range(i, len(abundant)):
            second = abundant[j]
            all_abundant_sums.add(first + second)

    non_sums = []
    for i in range(1, 28124):
        if i not in all_abundant_sums:
            non_sums.append(i)

    answer = sum(non_sums)
    print(answer)

if __name__ == '__main__':
    main()
