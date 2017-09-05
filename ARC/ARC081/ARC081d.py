def solve():
    n = int(input())
    pattern = [[a, b] for a, b in zip(list(input()), list(input()))]
    pointer, ans = 0, 0
    if pattern[0][0] == pattern[0][1]:
        ans = 3
    else:
        ans = 6
    while pointer < n - 1:
        current = pattern[pointer][0]
        if current == pattern[pointer][1]:
            if pattern[pointer+1][0] == pattern[pointer+1][1]:
                ans *= 2
                # print("X->X")
            else:
                ans *= 2
                # print("X->Y")
            pointer += 1
        else:
            if pointer + 2 >= n - 1:
                break
            if pattern[pointer+2][0] == pattern[pointer+2][1]:
                ans *= 1
                # print("Y->X")
            else:
                ans *= 3
                # print("Y->Y")
            pointer += 2
    print(ans % 1000000007)

if __name__=="__main__":
    solve()
