A, B, C, V = map(int, input().split())
S, T = map(int, input().split())
print(A * S + B * T - (0 if S + T < V else C * (S + T)))
