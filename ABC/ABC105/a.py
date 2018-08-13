#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n, k = map(int, input().split())
    print([0, 1][n%k>0])

if __name__=="__main__":
    solve()
