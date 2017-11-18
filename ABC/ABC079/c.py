l = list(input()) 
for i in range(8):
    p = ["+"if i&j else"-" for j in[1, 2, 4]]
    line = "".join([v+o for v,o in zip(l,p)]) + l[3]
    if eval(line) == 7:
        print(line + "=7")
        break
