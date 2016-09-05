import math

def solve():
    a, b, c = map(int, input().split())
    mindiff = 10 ** 27
    mindiff = min(mindiff, math.ceil(a/2) * b * c - math.floor(a/2) * b * c)
    mindiff = min(mindiff, math.ceil(b/2) * a * c - math.floor(b/2) * a * c)
    mindiff = min(mindiff, math.ceil(c/2) * b * a - math.floor(c/2) * b * a)
    print(mindiff)

if __name__=="__main__":
    solve()