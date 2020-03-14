def main():
    lim = int(input('Enter a positive integer: '))
    square_sum = (lim*(lim+1)/2)**2
    sum_square = sum(map(lambda x: x**2, range(lim + 1)))
    diff = square_sum - sum_square
    print(diff)

if __name__ == '__main__':
    main()