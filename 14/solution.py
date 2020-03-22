def collatz(n, steps):
    path = []
    cur = n
    while cur != 1:
        if cur in steps:
            return path, steps[cur]
        path.append(cur)
        cur = cur // 2 if cur % 2 == 0 else 3*cur + 1
    return path, 1

def main():
    lim = int(input('Enter limit: '))
    steps = {
        1: 1
    }
    for i in range(1, lim):
        path, addition = collatz(i, steps)
        for i in range(len(path)):
            num = path[i]
            steps[num] = len(path) - i + addition
    
    most = -1
    winner = None
    for start in steps:
        num_steps = steps[start]
        if start < lim and num_steps > most:
            most = num_steps
            winner = start
    print(winner)

if __name__ == '__main__':
    main()
