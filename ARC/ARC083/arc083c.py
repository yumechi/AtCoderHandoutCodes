import itertools

def solve():
    a, b, c, d, e, f = map(int, input().split())
    water_pair = []
    a_list = [a * i * 100 for i in range(f//(a * 100) + 1)]
    b_list = [b * i * 100 for i in range(f//(b * 100) + 1)]
    for elem in list(itertools.permutations(a_list + b_list, 2)):
        water_pair.append(elem[0] + elem[1])
    
    solt_max = int(f * ((100 * e) / (100 + e) / 100))
    water_pair = [i for i in set(water_pair) if f > i > 0]
    solt_pair = []
    c_list = [c * i for i in range(solt_max//c + 1)]
    d_list = [d * i for i in range(solt_max//b + 1)]
    for elem in list(itertools.permutations(c_list + d_list, 2)):
        solt_pair.append(elem[0] + elem[1])
    solt_pair = [i for i in set(solt_pair) if solt_max >= i]
    
    water_pair.sort()
    solt_pair.sort()
    max_pair = 0
    ans = [a * 100, 0]
    for water in water_pair:
        limit_solt = e * (water // 100)
        for solt in solt_pair:
            if solt > limit_solt:
                break
            if water + solt > f:
                break
            if (100 * solt) / (water + solt) > max_pair:
                max_pair = (100 * solt) / (water + solt)
                ans = [water + solt, solt]
    print(ans[0], ans[1])
    

if __name__=="__main__":
    solve()
