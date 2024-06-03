import sys
# credit to https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-the-user
# for info on how to read multi-line inputs in python
input = sys.stdin.read
data = input().strip().split()

index = 0
t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1

    arr = list(map(int, data[index:index + n]))
    index += n
    uniques = set()
    for item in arr:
        uniques.add(item)

    if (len(uniques) < n):
        print("NO")
    else:
        print("YES")
