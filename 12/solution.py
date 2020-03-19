import math

def get_triangular(n):
    return n*(n + 1)//2

def count_factors(n):
    if n == 1:
        return 1
    count = 2
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 2
    return count

def main():
    factor_target = int(input('Enter target number of factors: '))
    cur = 1
    while True:
        triangular = get_triangular(cur)
        factors = count_factors(triangular)
        if factors > factor_target:
            break
        cur += 1
    print(triangular)

if __name__ == '__main__':
    main()
