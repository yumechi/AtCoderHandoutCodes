list = [int(input()) for _ in range(3)]
slist = sorted(list)
for i in list:
    print(3 - slist.index(i))