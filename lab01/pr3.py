input1, input2 = map(int, input().split())
total = (input1 ** 2) + (input2 ** 2) + 1
if (total % 4 == 0):
    print(total/4)
else:
    print(-1)
