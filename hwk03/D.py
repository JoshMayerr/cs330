import sys


def dfs(grid, visited, i, j):
    stack = [(i, j)]
    volume = 0
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        volume += grid[x][y]
        for l, r in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            movex, movey = x + l, y + r
            if 0 <= movex < len(grid) and 0 <= movey < len(grid[0]) and grid[movex][movey] > 0 and (movex, movey) not in visited:
                stack.append((movex, movey))
    return volume


# def dfs(grid, visited, x, y):
#     if (x, y) in visited or grid[x][y] == 0:
#         return 0
#     visited.add((x, y))
#     volume = grid[x][y]
#     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         movex, movey = x + dx, y + dy
#         if 0 <= movex < len(grid) and 0 <= movey < len(grid[0]):
#             volume += dfs(grid, visited, movex, movey)
#     return volume


def max_volume(test_cases):
    results = []
    for grid in test_cases:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        max_volume = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and (i, j) not in visited:
                    volume = dfs(grid, visited, i, j)
                    max_volume = max(max_volume, volume)

        results.append(max_volume)
    return results


input = sys.stdin.read
data = input().strip().split()
index = 0
t = int(data[index])
index += 1

test_cases = []
for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    grid = []
    for i in range(n):
        row = list(map(int, data[index:index + m]))
        index += m
        grid.append(row)
    test_cases.append(grid)

results = max_volume(test_cases)

for result in results:
    print(result)
