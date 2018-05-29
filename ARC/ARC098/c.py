#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n = int(input())
    s = input()
    el, wl = [0]*n, [0]*n
    ec, wc = 0, 0
    for i in range(n):
        if s[n - 1 - i] == 'E':
            ec += 1
        if s[i] == 'W':
            wc += 1
        el[n - 1 - i] = ec
        wl[i] = wc

    ans = n - 1
    for i in range(n):
        if i == 0:
            ans = min(ans, el[i + 1])
        elif i == n - 1:
            ans = min(ans, wl[i - 1])
        else:
            ans = min(ans, wl[i - 1] + el[i + 1])
    print(max(0, ans))

if __name__=="__main__":
    solve()
