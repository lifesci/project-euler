import math

def amicability(num):
    amic = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            amic.add(i)
            if i > 1:
                amic.add(num//i)
    return sum(amic)

def main():
    lim = int(input('Enter limit: '))
    amicabilities = {}
    amicable_numbers = set()
    for i in range(1, lim + 1):
        amic = amicability(i)
        if amic not in amicabilities:
            amicabilities[amic] = []
        amicabilities[amic].append(i)
    
    # we now have a dictionary with structure { f(a): [a, ...] }
    # want to find pairs of the form { f(a): [a, ...], a: [f(a), ...] } such that a != f(a)
    for f_a in amicabilities:
        for a in amicabilities[f_a]:
            bs = amicabilities.get(a)
            if bs is not None:
                for b in bs:
                    if b != a and b == f_a:
                        amicable_numbers.add(f_a)
    print(sum(amicable_numbers))

if __name__ == '__main__':
    main()
