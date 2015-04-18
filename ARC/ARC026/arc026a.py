N, A, B = map(int, input().split())
print(B * N if N < 6 else B * 5 + A * (N - 5))