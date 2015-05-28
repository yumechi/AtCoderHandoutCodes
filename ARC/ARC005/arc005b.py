x, y, w = input().split()
x, y = int(x) - 1, int(y) - 1
table = [list(input()) for _ in range(9)]
res = ""
for _ in range(4):
    res += str(table[y][x])
    if "R" in w:
        x += 1
        if x > 8:
            x = 7
            w = w.replace("R", "L")
    elif "L" in w:
        x -= 1
        if x < 0:
            x = 1
            w = w.replace("L", "R")
    if "U" in w:
        y -= 1
        if y < 0:
            y = 1
            w = w.replace("U", "D")
    elif "D" in w:
        y += 1
        if y > 8:
            y = 7
            w = w.replace("D", "U")
 
print(res)