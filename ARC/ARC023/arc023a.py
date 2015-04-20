ylist = [int(input()) for _ in range(3)]
today = [2014, 5, 17]
ylist[0] -= 1 if ylist[1] < 3 else 0
ylist[1] += 12 if ylist[1] < 3 else 0
func = lambda l: 365 * l[0] + l[0] // 4 - l[0] // 100 + l[0] // 400 + (306 * (l[1] + 1)) // 10 + l[2] - 429
print(func(today) - func(ylist))