N = int(input())
maxscore = 0
for _ in range(N):
    a, b, c, d, e = map(int, input().split())
    score = sum([a, b, c, d, e * 110 / 900])
    maxscore = max(score, maxscore)
print(maxscore)