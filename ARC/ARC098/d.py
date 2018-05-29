#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n = int(input())
    al = [int(i) for i in input().split()]
    ss, xs = 0, 0
    
    ans = 0
    last_index = 0
    length = 0
    for i in range(n):
        ss += al[i]
        xs ^= al[i]
        length += 1
        while ss != xs:
            ss -= al[last_index]
            xs ^= al[last_index]
            last_index += 1
            length -= 1
        ans += length
    print(ans)

if __name__=="__main__":
    solve()
