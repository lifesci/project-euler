class Entry:
    def __init__(self, val):
        self.val = val
        self.prime = val >= 2
    
    def mark(self):
        self.prime = False

def sieve(limit):
    primes = []
    candidates = list(map(lambda x: Entry(x), range(limit)))
    index = 0
    while index < len(candidates):
        candidate = candidates[index]
        if candidate.prime:
            primes.append(candidate.val)
            factor = 2
            val = candidate.val
            ind = val*factor
            while ind < limit:
                candidates[ind].mark()
                factor += 1
                ind = val*factor
        index += 1
    return primes

def main():
    limit = int(input('Enter limit: '))
    primes = sieve(limit)
    print(sum(primes))

if __name__ == '__main__':
    main()