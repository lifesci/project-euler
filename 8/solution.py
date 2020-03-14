from functools import reduce

def read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    num = reduce(lambda x, y: x + y, lines, '')
    return num

def find_largest(num, window):
    start = 0
    largest = 0
    
    if len(num) < window:
        product = 1
        for digit in num:
            product *= int(digit)
        return cur
    
    while (start + window <= len(num)):
        prod = 1
        for digit in num[start:start+window]:
            prod *= int(digit)
        if prod > largest:
            largest = prod
        start += 1
    return largest

def main():
    window = int(input('Enter window size: '))
    num = read('./num.txt')
    largest = find_largest(num, window)
    print(largest)

if __name__ == '__main__':
    main()