n = input()
for a in sorted(enumerate([int(i) for i in input().split()]), key=lambda x: x[1])[::-1]:
    print(a[0]+1)
