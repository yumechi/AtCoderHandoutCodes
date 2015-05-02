a, b, c = map(int, input().split())
N = int(input())
calc = lambda mult, x: N * mult - x if N * mult > x else 0
print(calc(1, a), calc(2, b), calc(3, c))