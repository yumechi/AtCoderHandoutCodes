#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n, k = map(int, input().split())
    if n % 2 == 1:
        print("YES" if (n // 2 + 1) >= k else "NO")
    else:
        print("YES" if (n // 2) >= k else "NO")

if __name__=="__main__":
    solve()
