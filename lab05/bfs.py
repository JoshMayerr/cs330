# red = x * 2
# blue = x - 1
# go from n to m, no negative numbers

def bfs(s, d):
    q = []
    q.append(s)
    layer = {}
    layer[s] = 0
    visited = [s]
    while q:
        v = q.pop(0)
        if v == d:
            return layer[v]
        for i in [v-1, v*2]:
            if v > d and i > v:
                continue
            if i > 0 and i not in visited:
                visited.append(i)
                layer[i] = layer[v] + 1
                q.append(i)


n, m = map(int, input().split())
print(bfs(n, m))
