def solve():
    for c in input():
        if c in "aiueo":
            print("vowel")
            return
    print("consonant")


if __name__=="__main__":
    solve()