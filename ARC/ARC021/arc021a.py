def check(table):
    mx = [1, 0, -1, 0]
    my = [0, 1, 0, -1]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                x = j + mx[i]
                y = k + my[i]
                if 3 >= x >= 0 and 3 >= y >= 0 and table[j][k] == table[x][y]:
                    return True
    return False


table = []
for _ in range(4):
    alist = list(map(int, input().split()))
    table.append(alist)

print("CONTINUE" if check(table) else "GAMEOVER")