import sys


def bfs(start, visited, graph):
    q = [start]
    connected = []

    while q:
        v = q.pop(0)
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
        connected.append(v)

    return connected


def calc(n, m, costs, friends):
    G = {i: [] for i in range(n)}

    for x, y in friends:
        G[x - 1].append(y - 1)
        G[y - 1].append(x - 1)

    visited = set()
    total_cost = 0

    for i in range(n):
        if i not in visited:
            visited.add(i)
            component = bfs(i, visited, G)
            cost = min([costs[x] for x in component])
            total_cost += cost

    return total_cost


input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
m = int(data[1])
costs = [int(data[i]) for i in range(2, 2 + n)]
friends = [(int(data[i]), int(data[i + 1]))
           for i in range(2 + n, 2 + n + 2 * m, 2)]

print(calc(n, m, costs, friends))
