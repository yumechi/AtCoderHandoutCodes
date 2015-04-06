N = int(input())
S = input()
mt = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for c in S:
    mt[c] += 1
print((mt["A"] * 4 + mt["B"] * 3 + mt["C"] * 2 + mt["D"] * 1) / N)