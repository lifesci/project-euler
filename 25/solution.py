import math

def fib(limit):
    f_0 = 0
    f_1 = 1
    index = 1
    while math.log10(f_1) + 1 < limit:
        tmp = f_1
        f_1 = f_0 + f_1
        f_0 = tmp
        index += 1
    return index

def main():
    limit = int(input('Enter target number of digits: '))
    answer = fib(limit)
    print(answer)

if __name__ == '__main__':
    main()
