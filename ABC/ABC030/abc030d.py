N, a = map(int, input().split())
k = int(input())
bli = [int(i) - 1 for i in input().split()]
current = a-1
visited = [current]
for i in range(k):
    current = bli[current]
    if current in visited:
        subli = visited[visited.index(current):]
        print(subli[(k - len(visited) + len(subli)) % len(subli)] + 1)
        break
    else:
        visited.append(current)
else:
    print(current + 1)
