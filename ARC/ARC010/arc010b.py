N = int(input())
months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m_start_day = [0]
for i in range(0, 11):
    m_start_day.append(m_start_day[i] + months[i])

holi = [False for _ in range(0, 366)]
for i in range(0, 366):
    if i % 7 == 0 or i % 7 == 6:
        holi[i] = True

for _ in range(N):
    m, d = map(lambda x: int(x) - 1, input().split("/"))
    nowday = m_start_day[m] + d
    if holi[nowday]:
        i = 1
        while (nowday + i) <= 365 and holi[nowday + i]:
            i += 1
            if nowday + i >= 366:
                break
        else:
            if nowday + i <= 365:
                holi[nowday + i] = True
    else:
        holi[nowday] = True

count = 0
res = 0
for i in range(0, 366):
    if holi[i]:
        count += 1
    else:
        res = max(res, count)
        count = 0
else:
    res = max(res, count)
print(res)
