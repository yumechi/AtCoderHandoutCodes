#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n, k = map(int, input().split())
    ans = 0
    if n >= k:
        ans = (n - k + 1) / n
    al = [2 ** i for i in range(1, 18)]
    for i in range(1, min(n + 1, k)):
        for j in al:
            if i * j >= k:
                ans += (1 / n) * (1 / j)
                break
    print(ans)

if __name__=="__main__":
    solve()
