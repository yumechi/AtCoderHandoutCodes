list = reversed([input() for _ in range(4)])
for str in list:
    print("".join(reversed(str)))