print(sum([(lambda x:int(x[1])+1-int(x[0]))(input().split())for _ in[0]*int(input())]))
