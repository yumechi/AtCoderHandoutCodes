N, M = map(int, input().split())
name = list(input())
kit = list(input())
count = 0
dic = dict(zip(kit, [0 for _ in range(len(kit))]))
for c in name:
    if c not in kit:
        print(-1)
        break
    else:
        dic[c] -= 1
        if dic[c] < 0:
            count += 1
            for ch in kit:
                dic[ch] += 1
else:
    print(count)