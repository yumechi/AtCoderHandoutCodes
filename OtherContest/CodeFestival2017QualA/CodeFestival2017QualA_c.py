from collections import Counter

def solve():
    h, w = map(int, input().split())
    wd = dict(Counter(list("".join([input() for _ in range(h)]))))

    g1 = (w % 2) & (h % 2)
    g2 = (w % 2) * h//2 + (h % 2) * w//2
    g4 = h//2 * w//2
    
    for k in wd.keys():
        if (g1 > 0) and wd[k] % 4 == 1 or wd[k] % 4 == 3:
            g1 -= 1
            wd[k] -= 1
        while (g4 > 0) and wd[k] >= 4:
            g4 -= 1
            wd[k] -= 4
        while (g2 > 0) and wd[k] >= 2:
            g2 -= 1
            wd[k] -= 2
            
    print("No" if sum(wd.values()) else "Yes")
    
if __name__=="__main__":
    solve()
