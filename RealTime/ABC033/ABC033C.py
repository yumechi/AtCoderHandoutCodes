import sys
sys.setrecursionlimit(100000)
print(sum([1 for s in input().split("+") if eval(s) > 0]))