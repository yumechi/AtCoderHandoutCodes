#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n, k = map(int, input().split())
    s = input()
    print(s[:k - 1] + s[k - 1].lower() + s[k:])

if __name__=="__main__":
    solve()
