bli = "".join(input().split())
N = int(input())
ali = [input() for _ in range(N)]
for i in range(N):
    ali[i] = int(ali[i].translate(str.maketrans(bli, "0123456789")))
ali.sort()
for i in range(N):
    ali[i] = str(ali[i])
    ali[i] = ali[i].translate(str.maketrans("0123456789", bli))
    print(ali[i])
