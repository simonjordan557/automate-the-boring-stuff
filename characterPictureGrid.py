grid = [['.', '.', '.', '.', '.', '.'], \
        ['.', 'o', 'o', '.', '.', '.'], \
        ['o', 'o', 'o', 'o', '.', '.'], \
        ['o', 'o', 'o', 'o', 'o', '.'], \
        ['.', 'o', 'o', 'o', 'o', 'o'], \
        ['o', 'o', 'o', 'o', 'o', '.'], \
        ['o', 'o', 'o', 'o', '.', '.'], \
        ['.', 'o', 'o', '.', '.', '.'], \
        ['.', '.', '.', '.', '.', '.']]



for i in range(len(grid[0])):
    print()
    for j in range(len(grid)):
        print(grid[j][i], end='')
    
