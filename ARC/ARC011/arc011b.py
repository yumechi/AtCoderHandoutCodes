_ = int(input())
dic = {"b": 1, "c": 1, "d": 2, "w": 2, "t": 3, "j": 3, "f": 4, "q": 4, "l": 5, "v": 5, "s": 6, "x": 6, "p": 7, "m": 7,
       "h": 8, "k": 8, "n": 9, "g": 9, "z": 0, "r": 0}
res = []
for s in input().split():
    resst = ""
    for c in s:
        if c.isalpha():
            c = c.lower()
        if c in dic:
            resst += str(dic[c])
    if not resst == "":
        res.append(resst)
print(" ".join(res) if len(res) > 0 else "")