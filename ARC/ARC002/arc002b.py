Y, M, D = map(int, input().split("/"))
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while not (Y % M == 0 and (Y // M) % D == 0):
    D += 1
    if D > month[M]:
        if M == 2 and D == 29 and ((Y % 400 == 0 or Y % 100 != 0) and Y % 4 == 0):
            continue
        if M == 12:
            Y += 1
            M = 1
        else:
            M += 1
        D = 1
print("%04d/%02d/%02d" % (Y, M, D))