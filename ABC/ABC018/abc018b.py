# 書き直したいなあ…

S = input()
N = int(input())
for i in range(0, N):
    l1, r1 = map(int, input().split())
    l1 -= 1
    r1 -= 1
    temp = []
    if l1 == 0 and (r1 == (len(S) - 1)):
        temp = S[::-1]
    elif l1 == 0:
        temp = S[r1::-1] + S[r1 + 1:]
    elif r1 == len(S) - 1:
        temp = S[:l1] + S[r1:l1 - 1:-1]
    else:
        temp = S[:l1] + S[r1:l1 - 1:-1] + S[r1 + 1:]
    S = temp

print(S)