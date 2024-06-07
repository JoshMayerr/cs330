n, a, b, c = map(int, input().split())

byA = (n % a) == 0
byB = (n % b) == 0
byC = (n % c) == 0

if ((byA and not byB) or byC):
    print("YES")
else:
    print("NO")
