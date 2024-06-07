n, d = map(int, input().split())
a = list(map(int, input().split()))
poke = {}

for i in a:
    poke[i] = 1

for t in poke:
    if (t + d in poke):
        poke[t+d] += 1

print(sum([1 for i in poke if i > 1]))
# ddd
