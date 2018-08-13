#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n = int(input())
    ans, m = "", 1
    while n != 0:
        m *= (-2)
        if abs(n) % abs(m) > 0:
            ans += "1"
            n -= m // (-2)
        else:
            ans += "0"
    print(ans[::-1] if ans else 0)

if __name__=="__main__":
    solve()
