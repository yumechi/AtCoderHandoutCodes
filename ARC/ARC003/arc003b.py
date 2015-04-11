# from my smartphone
N = int(input())
wordlist = []
for _ in range(N):
    s = input()
    wordlist.append(s[::-1])
wordlist.sort()
for s in wordlist:
    print(s[::-1])