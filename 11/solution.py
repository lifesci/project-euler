def read(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]
    lines = [list(map(lambda x: int(x), line.split(' '))) for line in lines]
    return lines

def horizontal(window, row, col, rows, cols, lines):
    if col + window <= cols:
        product = 1
        for i in range(col, col + window):
            product *= lines[row][i]
        return product
    else:
        return 0

def vertical(window, row, col, rows, cols, lines):
    if row + window <= rows:
        product = 1
        for i in range(row, row + window):
            product *= lines[i][col]
        return product
    else:
        return 0

def diagonal_down(window, row, col, rows, cols, lines):
    if row + window <= rows and col + window <= cols:
        product = 1
        for i in range(window):
            product *= lines[row + i][col + i]
        return product
    else:
        return 0

def diagonal_up(window, row, col, rows, cols, lines):
    if row - window >= -1 and col + window <= cols:
        product = 1
        for i in range(window):
            product *= lines[row - i][col + i]
        return product
    else:
        return 0

def main():
    window = int(input('Enter window size: '))
    lines = read('./grid.txt')
    rows = len(lines)
    cols = len(lines[0])
    
    largest = 0
    
    row = None
    col = None
    direction = None
    
    for i in range(rows):
        for j in range(cols):
            horiz = horizontal(window, i, j, rows, cols, lines)

            vert = vertical(window, i, j, rows, cols, lines)

            diag_down = diagonal_down(window, i, j, rows, cols, lines)
            
            diag_up = diagonal_up(window, i, j, rows, cols, lines)
            
            largest = max(largest, horiz, vert, diag_down, diag_up)
            
    print(largest)

if __name__ == '__main__':
    main()