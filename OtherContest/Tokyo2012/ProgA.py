Y, M, D = input().split("/")
print("yes" if sorted(list(Y)) == sorted(list(M+D)) else "no")