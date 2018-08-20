#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve():
    s = input()
    n = int(input())
    idx = 0
    slen = len(s)
    while idx < slen and s[idx] == "1":
        idx += 1
        if idx == n:
            print(1)
            return
    if idx == slen:
        print(1)
    else:
        print(s[idx])


if __name__ == "__main__":
    solve()
