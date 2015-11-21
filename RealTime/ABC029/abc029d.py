n = int(input())
res = 0
for i in range(len(str(n))):
    nowdigit = 10 ** (i + 1)
    partnum = n % nowdigit
    partdigit = 10 ** i

    res += n // nowdigit * partdigit
    
    if partnum >= 2 * partdigit:
        res += partdigit
    elif 2 * partdigit > partnum >= partdigit:
        res += partnum - partdigit + 1
print(res)
