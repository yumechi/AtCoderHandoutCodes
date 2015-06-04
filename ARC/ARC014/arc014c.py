N, S = input(), input()
f = lambda c: S.count(c) % 2
print(f("R") + f("G") + f("B"))
