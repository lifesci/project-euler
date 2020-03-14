import math

def is_prime(n):
    root = int(math.sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0:
            return False
    return True

def main():
    lim = int(input('Enter a positive integer: '))
    found = 0
    cur = 1
    while(found < lim):
        cur += 1
        if is_prime(cur):
            found += 1
    print(cur)

if __name__ == '__main__':
    main()