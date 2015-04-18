A, B = map(lambda x: abs(int(x)), input().split())
if A == B:
    print("Draw")
else:
    print("Ant" if A < B else "Bug")