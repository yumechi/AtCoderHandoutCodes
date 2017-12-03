#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n = int(input())
    fl = [[int(i) for i in input().split()] for _ in range(n)]
    pl = [[int(i) for i in input().split()] for _ in range(n)]
    ans = -1 * 100 * (10 ** 7)
    for cnt in range(1, 2 ** 10 + 1):
        cnt_list = [0]*n
        for i in range(n):
            t = cnt
            digit = 0
            while t > 0:
                if t & 1 != 0 and fl[i][digit - 1] == 1:
                  cnt_list[i] += 1
                t >>= 1
                digit += 1
        tsum = 0
        for i in range(n):
            tsum += pl[i][cnt_list[i]]
        ans = max(tsum, ans)
    print(ans)


if __name__=="__main__":
    solve()
