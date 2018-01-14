#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n, y = map(int, input().split())
    y //= 1000

    for noguchi in range(n + 1):
        for higuchi in range(n + 1 - noguchi):
            yukichi = n - noguchi - higuchi
            if noguchi + higuchi * 5 + yukichi * 10 == y:
                print(yukichi, higuchi, noguchi)
                return
    
    print("-1 -1 -1")

if __name__=="__main__":
    solve()
