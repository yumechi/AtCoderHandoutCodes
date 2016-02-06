import itertools
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
ei, choku, don = 0, 0, 0
calclengths = lambda x1, y1, x2, y2: \
    abs((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
for elems in list(itertools.combinations(points, 3)):
    i = calclengths(elems[0][0], elems[0][1], elems[1][0], elems[1][1])
    j = calclengths(elems[1][0], elems[1][1], elems[2][0], elems[2][1])
    k = calclengths(elems[2][0], elems[2][1], elems[0][0], elems[0][1])
    temp = sorted([i, j, k])
    if temp[2] == temp[1] + temp[0]:
        choku += 1
    elif temp[2] > temp[1] + temp[0]:
        don += 1
    else:
        ei += 1
print(ei, choku, don)