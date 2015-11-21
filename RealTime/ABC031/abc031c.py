n = int(input())
ali = [int(i) for i in input().split()]
res = -10000
# i = takahashi select, j = aoki select
for i in range(n):
    taoki, ttakah = -10000, -10000
    ti = i
    aidx = -1
    for j in range(n):
        parlist = ali[i:j+1] if i < j else ali[j:i+1]
        parlength = len(parlist)
        if i == j or parlength < 2:
            continue

        nowaoki, nowtakah = 0, 0
        for k in range(parlength):
            if k % 2 == 0:
                nowtakah += parlist[k]
            else:
                nowaoki += parlist[k]

        if nowaoki > taoki:
            taoki = nowaoki
            ttakah = nowtakah
            aidx = j
        elif nowaoki == taoki and j < aidx:
            taoki = nowaoki
            ttakah = nowtakah
            aidx = j
    res = max(res, ttakah)
print(res)
