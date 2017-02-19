def solve():
    n = int(input())
    work_array = [[a, b] for a, b in zip([int(i) for i in input().split()], [j for j in range(0, n)])]
    ans_list = [0] * n
    work_array.sort(reverse=True)

    last_num = work_array[0][0]
    min_index = work_array[0][1]
    for counter in range(n):
        current_num = work_array[counter][0]
        if last_num != current_num:
            ans_list[min_index] += counter * (last_num - current_num)
            last_num = current_num
        min_index = min(min_index, work_array[counter][1])

    ans_list[min_index] += (counter + 1) * last_num
    print("\n".join([str(c) for c in ans_list]))

if __name__=="__main__":
    solve()
