s = list(map(int, list(input())))
if len(s) == 1:
    print(0, sum(s))
else:
    if len(s) % 2 == 1:
        print(sum(s[1::2]), sum(s[::2]))
    else:
        print(sum(s[::2]), sum(s[1::2]))