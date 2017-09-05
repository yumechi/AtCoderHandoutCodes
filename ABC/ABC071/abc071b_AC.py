print((lambda x:"None" if not x else x[0])(sorted(set(chr(97+i) for i in range(26))-set(list(input())))))
