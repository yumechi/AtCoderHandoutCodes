S = input()
T = input()

if len(S) != len(T):
    print("-1")
    exit()

length = len(S)

for i in range(0, length):
    if S == T:
        print(i)
        exit()
    else:
        S = S[-1:] + S[0:length - 1]
else:
    print("-1")
