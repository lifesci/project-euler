def main():
    target = 1000
    
    lim = 500
    
    for i in range(1, lim + 1):
        for j in range(1, lim + 1):
            for k in range(1, lim + 1):
                if (i**2 + j**2) == k**2 and i + j + k == target:
                    print(i*j*k)
                    return

if __name__ == '__main__':
    main()