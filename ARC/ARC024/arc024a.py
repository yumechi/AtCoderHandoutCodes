L, R = map(int, input().split())
Llist = list(map(int, input().split()))
Rlist = list(map(int, input().split()))
for shoeL in Llist:
    if shoeL in Rlist:
        Rlist.remove(shoeL)
print(R - len(Rlist))