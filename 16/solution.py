def sum_digits(num):
    return sum([int(i) for i in str(num)])

def main():
    # use the fact that python can handle arbitrarily large numbers
    num = 2**1000
    print(sum_digits(num))

if __name__ == '__main__':
    main()
