#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n = int(input())
    l4 = [4 * i for i in range(25)]
    l7 = [7 * i for i in range(15)]
    for a in l4:
        for b in l7:
            if a + b == n:
                print("Yes")
                return
    print("No")

if __name__=="__main__":
    solve()
