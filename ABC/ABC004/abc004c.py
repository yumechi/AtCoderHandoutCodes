N = int(input())
l = [int(i) for i in range(1, 7)]
m = [int(i) for i in range(1, 7)]

patterns = []
flag = True
i = 0
while (flag):
    patterns.append(list(l))
    j = (i % 5)
    l[j], l[j + 1] = l[j + 1], l[j]
    i += 1
    if l == m:
        flag = False

print("".join(map(str, patterns[N % i])))