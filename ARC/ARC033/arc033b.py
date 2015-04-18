Na, Nb = map(int, input().split())
setA = set(list(map(int, input().split())))
setB = set(list(map(int, input().split())))
print(len(setA & setB) / len(setA | setB))