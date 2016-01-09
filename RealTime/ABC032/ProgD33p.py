N, W = map(int, input().split())
viwi = [[int(x) for x in input().split()] for _ in range(N)]

if N <= 30:
    dp = {}
    for i in range(N):
        vi, wi = viwi[i][0], viwi[i][1]
        adddic = {}
        for k, v in dp.items():
            if (k + wi) <= W:
                if (k + wi) in dp:
                    adddic[k + wi] = max(dp[k] + vi, dp[k + wi])
                else:
                    adddic[k + wi] = dp[k] + vi
        if wi <= W:
            adddic[wi] = vi
        dp.update(adddic)
    print(max(dp.values()))
else:
    wmax = 0
    wsum = 0
    for i in range(N):
        wmax = max(wmax, viwi[i][1])
        wsum += viwi[i][1]
    if wmax <= 1000:
        dp = {}
        for i in range(N):
            vi, wi = viwi[i][0], viwi[i][1]
            adddic = {}
            for k, v in dp.items():
                if (k + wi) in dp:
                    adddic[k + vi] = min(dp[k] + wi, dp[k + vi])
                else:
                    adddic[k + vi] = dp[k] + wi
            adddic[vi] = wi
            dp.update(adddic)
        res = 0
        for k, v in dp.items():
            if v <= W:
                res = max(res, k)
        print(res)
    else:
        dp = {}
        for i in range(N):
            vi, wi = viwi[i][0], viwi[i][1]
            adddic = {}
            for k, v in dp.items():
                if (k + vi) in dp:
                    adddic[k + vi] = min(dp[k] + wi, dp[k + vi])
                else:
                    adddic[k + vi] = dp[k] + wi
            adddic[vi] = wi
            dp.update(adddic)
        res = 0
        for k, v in dp.items():
            if v <= W:
                res = max(res, k)
        print(res)
