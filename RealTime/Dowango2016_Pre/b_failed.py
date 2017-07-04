def solve():
    niconico_str = input()
    str_length = len(niconico_str)
    ans = 0
    for index, n_char in enumerate(niconico_str):
        if n_char == "2" or n_char == "5":
            pointer = index - 1
            flag_2 = 
            tlength = 1
            while pointer >= 0:
                if niconico_str[pointer] == "?":
                    tlength += 1
                else:
                    if flag_2:
                            if niconico_str[pointer] == "5":
                                tlength += 1
                            else:
                                break
                    else:
                            if niconico_str[pointer] == "2":
                                tlength += 1
                            else:
                                break
                flag_2 = !flag_2
                pointer -= 1
            pointer = index + 1
            flag_2 = True
            while pointer < str_length:
                if niconico_str[pointer] == "?":
                    tlength += 1
                else:
                    if flag_2:
                            if niconico_str[pointer] == "5":
                                tlength += 1
                            else:
                                break
                    else:
                            if niconico_str[pointer] == "2":
                                tlength += 1
                            else:
                                break
                flag_2 = !flag_2
                pointer -= 1



if __name__=="__main__":
    solve()
