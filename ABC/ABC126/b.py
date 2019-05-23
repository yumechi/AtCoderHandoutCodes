#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    s = input()
    f, t = s[:2], s[2:]
    YYMM = 0 <= int(f) <= 99 and 1 <= int(t) <= 12
    MMYY = 0 <= int(t) <= 99 and 1 <= int(f) <= 12
    if YYMM and MMYY:
        print('AMBIGUOUS')
    elif YYMM:
        print('YYMM')
    elif MMYY:
        print('MMYY')
    else:
        print('NA')

if __name__=="__main__":
    solve()
