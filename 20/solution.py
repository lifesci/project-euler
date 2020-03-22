import math

def main():
    target = int(input('Enter factorial for which to count digits: '))
    num = str(math.factorial(target))
    total = sum([int(digit) for digit in num])
    print(total)

if __name__ == '__main__':
    main()
