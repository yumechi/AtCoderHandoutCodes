N, A, B = map(int, input().split())
turn = 1
while N > 0:
    turn += 1
    N -= A if turn % 2 == 0 else B
print("Ant" if turn % 2 == 0 else "Bug")