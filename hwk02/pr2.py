import sys
# credit to https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-the-user
# for info on how to read multi-line inputs in python
input = sys.stdin.read
data = input().strip().split()

n = data[0]
m = int(data[1])
items = [int(x) for x in data[2:]]

print(abs(sum(sorted([x for x in items if x < 0])[:m])))
