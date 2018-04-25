#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    w = int(input())
    n, k = map(int, input().split())
    widths, rarities = [], []
    for i in range(n):
        a, b = map(int, input().split())
        widths.append(a)
        rarities.append(b)
    
    dp = [[0 for i in range(w + 1)] for _ in range(k + 1)]

    for i in range(n):
        for j in range(w, 0, -1):
            for l in range(1, k):
                if dp[l][j] > 0 and j + widths[i] <= w:
                    dp[l + 1][j + widths[i]] = max(dp[l + 1][j + widths[i]],
                            dp[l][j] + rarities[i])
        if widths[i] <= w:
            dp[1][widths[i]] = max(dp[1][widths[i]], rarities[i])
    print(max([max(dp[i]) for i in range(1, k + 1)]))

if __name__=="__main__":
    solve()
