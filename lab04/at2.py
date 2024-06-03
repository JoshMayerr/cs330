import sys
input = sys.stdin.read
data = input().strip().split()

n = int(data[0])
A = [int(x) for x in data[1:n+1]]
B = [int(x) for x in data[n+1:]]

total = 0
for i in range(n):
    total += A[i] ** B[i]

print(total % 2)
