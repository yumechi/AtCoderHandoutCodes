from collections import Counter

def solve():
    c = Counter(input())
    print("Yes" if ((c["N"] > 0 and c["S"] > 0) or c["N"] == c["S"]) \
     and ((c["E"] > 0 and c["W"] > 0) or c["E"] == c["W"]) else "No")

if __name__=="__main__":
    solve()