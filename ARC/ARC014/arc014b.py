N = int(input())
prev = [] # prev said
ckecker = lambda ls, s, prev: ls[-1:] != s[0] or s in prev
last = ""

for i in range(1, N + 1):
    s = input()
    if i != 1 and ckecker(last, s, prev):
        print("LOSE" if i % 2 == 1 else "WIN")
        exit(0)
    prev.append(s)
    last = s
else:
    print("DRAW")