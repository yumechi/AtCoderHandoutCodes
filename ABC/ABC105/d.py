#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    al = [int(i) for i in input().split()]
    bl = [0]*n
    d = defaultdict(int)
    for i in range(n):
        bl[i] = (al[i] + bl[max(0, i - 1)]) % m
        d[bl[i]] += 1
    ans = 0
    for k, v in d.items():
        if k == 0:
            v = v + 1
        ans += v * (v - 1) // 2
    print(ans) 

if __name__=="__main__":
    solve()
