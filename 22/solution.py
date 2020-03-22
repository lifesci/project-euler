def calc_value(name, position):
    value = 0
    for char in name:
        value += ord(char) - ord('A') + 1
    return value*position

def read_names(filename):
    with open(filename) as f:
        content = f.read()
    content = content.strip()
    names = content.split(',')
    names = [name[1:-1] for name in names]
    return names

def main():
    names = read_names('./names.txt')
    names.sort()
    total = 0
    for i in range(len(names)):
        name = names[i]
        total += calc_value(name, i + 1)
    print(total)

if __name__ == '__main__':
    main()
