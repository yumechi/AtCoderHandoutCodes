print("Yes" if (lambda x: int(x[1:]) % 111 == 0 or int(
    x[:-1]) % 111 == 0)(input()) else "No")
