#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    n, c = map(int, input().split())
    c_info = [[int(i) for i in input().split()] for _ in range(n)]
    c_info.sort(key=lambda x: (x[2], x[0]))
    info = []
    cnt = 0
    
    while cnt < n:
        if cnt == n - 1:
            info.append(c_info[cnt])
            break
        if c_info[cnt][1] == c_info[cnt + 1][0] and c_info[cnt][2] == c_info[cnt + 1][2]:
            tc = c_info[cnt][2]
            t = [c_info[cnt][0], c_info[cnt + 1][1], tc]
            cnt += 1
            while cnt < n - 1 and t[1] == c_info[cnt + 1][0] and tc == c_info[cnt + 1][2]:
                t = [t[0], c_info[cnt + 1][1], tc]
                cnt += 1
            info.append(t)
            if cnt == n - 1:
                break
        else:
            info.append(c_info[cnt])
        cnt += 1

    tarr = [0] * (2 + 10 ** 5)
    for elem in info:
       tarr[elem[0]] += 1
       tarr[elem[1] + 1] -= 1
    
    ans = 1
    tans = 0
    for elem in tarr:
        tans += elem
        ans = max(ans, tans)
    print(ans)

if __name__=="__main__":
    solve()
