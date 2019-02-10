#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

def solve():
    cnt = defaultdict(int)
    for i in range(3):
        a, b = input().split()
        cnt[a] += 1
        cnt[b] += 1
    ok = len(cnt.keys()) == 4
    one, two = 0, 0
    for v in cnt.values():
        if v == 1:
            one += 1
        if v == 2:
            two += 1
    ok = ok and (one == 2 and two == 2)
    print("YES" if ok else "NO")
    

if __name__=="__main__":
    solve()
