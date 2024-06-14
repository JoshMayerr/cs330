import sys


def is_cycle(component, graph):
    for node in component:
        if len(graph[node]) != 2:
            return False
    return True


def bfs(start, visited, graph):
    q = [start]
    connected = []

    while q:
        v = q.pop(0)
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                connected.append(neighbor)

    print(connected)

    return connected


def count(n, m, edges):
    G = {i: [] for i in range(n)}

    for x, y in edges:
        G[x].append(y)
        G[y].append(x)

    visited = set()
    all_components = []

    for i in range(n):
        if i not in visited:
            component = bfs(i, visited, G)
            all_components.append(component)

    count = 0
    for component in all_components:
        if len(component) > 2 and is_cycle(component, G):
            count += 1

    return count


input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
m = int(data[1])
edges = [(int(data[i]) - 1, int(data[i + 1]) - 1)
         for i in range(2, 2 + 2 * m, 2)]

print(count(n, m, edges))
