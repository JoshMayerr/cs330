import sys
# credit to https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-the-user
# for info on how to read multi-line inputs in python
input = sys.stdin.read
data = input().strip().split()

n = int(data[0])
ints = [int(x) for x in data[1:]]
start, end = -1, -1
for i in range(1, len(ints)):
    if ints[i] < ints[i - 1]:
        if start == -1:
            start = i - 1
        end = i

if start == -1:
    print('yes')
    print(1, 1)
else:
    seg = ints[start:end + 1]
    rev = seg[::-1]
    arr = ints[:start] + rev + ints[end+1:]
    if arr == sorted(ints):
        print('yes')
        print(start+1, end+1)
    else:
        print('no')
