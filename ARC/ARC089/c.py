#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    x, y, t = 0, 0, 0
    for i in range(int(input())):
        tt, tx, ty = map(int, input().split())
        m = abs(x - tx) + abs(y - ty)
        if m > (tt - t):
            print("No")
            return
        if (m - (tt - t)) % 2 == 1:
            print("No")
            return
        x, y, t = tx, ty, tt
    print("Yes")

if __name__=="__main__":
    solve()
