N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
maxbox = [0, 0, 0]
for elem in table:
    elem.sort(reverse=True)
    for i in range(3):
        maxbox[i] = max(maxbox[i], elem[i])
print(maxbox[0] * maxbox[1] * maxbox[2])