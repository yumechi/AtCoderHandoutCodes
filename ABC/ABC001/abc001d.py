list = [False for i in range(12 * 24 + 1)]
N = eval(input())
for i in range(N):
    start, end = map(int, input().split("-"))
    start -= start % 5
    end += 4
    end -= end % 5
    s = (start // 100 * 12) + (start % 100) // 5
    e = (end // 100 * 12) + (end % 100) // 5
    for j in range(s, e):
        list[j] = True

count = 0
while count < 12 * 24 + 1:
    if list[count]:
        pstart = 100 * int(count / 12) + 5 * (count % 12)
        while list[count]:
            count += 1
        pend = 100 * int(count / 12) + 5 * (count % 12)
        print(str(int(pstart)).zfill(4) + "-" + str(int(pend)).zfill(4))
    else:
        count += 1