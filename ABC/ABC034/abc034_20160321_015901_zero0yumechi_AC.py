MOD = 10**9+7
 
def mycombi(n, r, m):
    res = 1
    for i in range(r):
        res *= (n-i) * pow(r-i, m-2, m)
        res %= m
    return res
 
def solve():
    w, h = map(int, input().split())
    res = 1
    print(mycombi(w+h-2, min(w, h)-1, MOD))
 
if __name__=="__main__":
    solve()
