from sys import stdin
from collections import deque

#dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#bfs
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


#입력
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(N+1):
    graph[i].sort()

visited = [False]*(N+1)
dfs(graph, V, visited)
print("")
visited = [False]*(N+1)
bfs(graph, V, visited)