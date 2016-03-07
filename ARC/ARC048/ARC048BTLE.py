n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if data[i][0] != data[j][0]:
            if data[i][0] > data[j][0]:
                result[i][0] += 1
                result[j][1] += 1
            else:
                result[i][1] += 1
                result[j][0] += 1
        else:
            matchresult = (data[i][1] - data[j][1] + 3) % 3
            if matchresult == 0:
                result[i][2] += 1
                result[j][2] += 1
            elif matchresult == 2:
                result[i][0] += 1
                result[j][1] += 1
            else:
                result[i][1] += 1
                result[j][0] += 1

for elem in result:
    print(" ".join(map(str, elem)))