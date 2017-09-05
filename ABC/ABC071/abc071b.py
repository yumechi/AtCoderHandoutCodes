print((lambda x:"None" if not x else min(x))(set(chr(97+i) for i in range(26))-set(input())))
