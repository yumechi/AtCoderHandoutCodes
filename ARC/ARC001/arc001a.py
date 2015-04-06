N, S = int(input()), input()
maxnum = int(max(S.count("1"), S.count("2"), S.count("3"), S.count("4")))
minnum = int(min(S.count("1"), S.count("2"), S.count("3"), S.count("4")))
print(maxnum, minnum)