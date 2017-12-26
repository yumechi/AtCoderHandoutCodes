#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    s = input()
    xa, ya = map(int, input().split())
    xset = set([0])
    yset = set([0])

    if "T" not in s:
        print("Yes" if len(s) == xa and ya == 0 else "No")
        return

    fcnt = 0
    tcnt = 0
    for c in s:
        if "T" == c:
            if fcnt > 0:
                if tcnt % 2 == 0:
                    if tcnt == 0:
                        xset = set([x + fcnt for x in xset]) 
                    else:
                        xset = set([x + fcnt for x in xset]) | set([x - fcnt for x in xset])
                else:
                    yset = set([y + fcnt for y in yset]) | set([y - fcnt for y in yset])
            fcnt = 0
            tcnt += 1
        if "F" == c:
            fcnt += 1

    if fcnt > 0:
        if tcnt % 2 == 0:
            if tcnt == 0:
                xset = set([x + fcnt for x in xset]) 
            else:
                xset = set([x + fcnt for x in xset]) | set([x - fcnt for x in xset])
        else:
            yset = set([y + fcnt for y in yset]) | set([y - fcnt for y in yset])
    
    print("Yes" if (xa in xset) and (ya in yset) else "No")

if __name__=="__main__":
    solve()
