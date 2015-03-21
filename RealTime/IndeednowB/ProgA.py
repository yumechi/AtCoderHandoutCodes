import math

X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())

print(str(int(math.fabs(X1 - X2) + math.fabs(Y1 - Y2) + 1)))