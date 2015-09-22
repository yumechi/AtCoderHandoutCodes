d = {"t":0, "i":0, "e":0, "c":0, "h":0}
for c in input():
    if c not in d:
        print("No")
        exit(0)
    else:
        d[c] += 1
if (d["t"] % 2 == 0) and (d["t"] // 2 == d["i"] == d["e"] == d["c"] == d["h"]):
    print("Yes")
else:
    print("No")
