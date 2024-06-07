import sys


def bfs(n, employees):
    graph = {}
    layer = {}

    for i in range(1, n + 1):
        if employees[i - 1] != -1:
            if employees[i - 1] not in graph:
                graph[employees[i - 1]] = []
            graph[employees[i - 1]].append(i)

    queue = []

    for i in range(1, n + 1):
        if employees[i - 1] == -1:
            queue.append(i)
            layer[i] = 1

    while queue:
        current = queue.pop(0)
        if current in graph:
            for neighbor in graph[current]:
                queue.append(neighbor)
                layer[neighbor] = layer[current] + 1

    return max(layer.values())


input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
employees = [int(x) for x in data[1:]]
print(bfs(n, employees))
