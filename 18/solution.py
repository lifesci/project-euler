def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [line.strip() for line in content]
    content = [[int(i) for i in line.split(' ')] for line in content]
    return content

def get_parent(i, j, graph, left):
    if i == 0:
        return 0
    if left:
        if j == 0:
            return 0
        return graph[i-1][j-1]
    else:
        if j >= len(graph[i-1]):
            return 0
        return graph[i-1][j]

def main():
    filename = input('Enter file name: ')
    graph = read_file(f'./{filename}')
    for i in range(len(graph)):
        row = graph[i]
        for j in range(len(row)):
            value = row[j]
            lparent = get_parent(i, j, graph, True)
            rparent = get_parent(i, j, graph, False)
            graph[i][j] = value + max(lparent, rparent)
    print(max(graph[-1]))

if __name__ == '__main__':
    main()
