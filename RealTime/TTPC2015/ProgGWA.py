from collections import Counter

s = input()
d = Counter(s)
# illegal word count
if len(s) % 6 == 0 or not ((d["t"] % 2 == 0) and (d["t"] // 2 == d["i"] == d["e"] == d["c"] == d["h"])):
    print("No")
