import array

def solve():
    n, m = map(int, input().split())
    humanSpeakLanguages = []
    for _ in range(n):
        language = array.array("I", [int(i) for i in input().split()])
        humanSpeakLanguages.append(language[1:])
    stack = set(humanSpeakLanguages[0])
    humanSpeakLanguages.pop(0)
    while len(humanSpeakLanguages) > 0:
        stacklength = len(stack)
        removeIdxs = array.array("I")
        for (i, language) in enumerate(humanSpeakLanguages):
            lset = set(language)
            if len(lset & stack):
                stack |= lset
                removeIdxs.append(i)

        for elem in removeIdxs[::-1]:
            humanSpeakLanguages.pop(elem)

        if stacklength == len(stack):
            break

    if len(humanSpeakLanguages) > 0:
        print("NO")
    else:
        print("YES")

if __name__=="__main__":
    solve()