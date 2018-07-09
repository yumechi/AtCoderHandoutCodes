#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    a, b = map(int, input().split())
    ans = "x"
    if a + b == 15:
        ans = "+"
    if a * b == 15:
        ans = "*"
    print(ans)

if __name__=="__main__":
    solve()
