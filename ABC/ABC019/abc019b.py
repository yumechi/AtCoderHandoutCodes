s = input()
res = last = ""
count = 1
for c in s:
    if last == "":
        last = c
        continue
    if last == c:
        count += 1
    else:
        res += last + str(count)
        count = 1
    last = c
else:
    res += last + str(count)
    print(res)