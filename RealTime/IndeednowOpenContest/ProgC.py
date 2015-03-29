N, M = map(int, input().split())
companies = []
for _ in range(0, N):
    temp = list(map(int, input().split()))
    companies.append(temp)
companies.sort(key=lambda x:(x[3],x[0],x[1],x[2]), reverse=True)

for _ in range(0, M):
    hunter = list(map(int, input().split()))
    maxsalary = 0
    for company in companies:
        if company[0] > hunter[0]:
            continue
        if company[1] > hunter[1]:
            continue
        if company[2] > hunter[2]:
            continue
        maxsalary = company[3]
        break
    print(maxsalary)