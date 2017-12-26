#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

def solve():
    n = int(input())
    ad = defaultdict(int)
    for i in input().split():
       ad[int(i)] += 1
    
    ans = 0
    for k, v in ad.items():
        if k > v:
            ans += v
        if v > k:
            ans += v - k
    print(ans)

if __name__=="__main__":
    solve()
