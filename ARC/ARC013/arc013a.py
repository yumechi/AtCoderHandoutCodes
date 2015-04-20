import itertools

balllist = list(map(int, input().split()))
baglist = list(map(int, input().split()))
func = lambda x, y: x // y
reslist = []
for l in itertools.permutations(baglist):
    bag = 1
    for i in range(3):
        bag *= func(balllist[i], l[i])
    reslist.append(bag)
print(int(max(reslist)))
