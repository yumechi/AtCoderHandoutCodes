def solve():
    from collections import Counter
    s = [i for i in sorted(Counter(input()).values())]
    t = [i for i in sorted(Counter(input()).values())]
    print(["No", "Yes"][s == t])


solve()
