str = input()

c = sum([1 for x in str if x == 'O'])
if (c == 1):
    print("Ya")
else:
    print("Tidak")
