import sys
input = sys.stdin.read
data = input().strip().split()

n = int(data[0])
laptops = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]

laptops.sort()

alex_happy = False
for i in range(1, n):
    if laptops[i-1][1] > laptops[i][1]:
        alex_happy = True
        break

if alex_happy:
    print("Happy Alex")
else:
    print("Poor Alex")
