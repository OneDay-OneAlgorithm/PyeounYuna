from sys import stdin
input = stdin.readline

from collections import deque

def bfs(graph, visited, m, n):
    dx = [1, -1, 0, 0] #오, 왼, 상, 하
    dy = [0, 0, -1, 1]
    queue = deque([(0,0)]) #x, y
    z_cnt = 0 #지렁이 갯수 카운트

    for ix in range(m):
        for iy in range(n):
            #방문 x고, 그래프에서 배추가 심어져있다면
            if not visited[iy][ix] and graph[iy][ix]:
                z_cnt +=1
                queue.append((ix,iy))
                while queue:
                    v = queue.popleft() #하나 꺼내고
                    # 네 방향 탐색
                    for i in range(4):
                        #벗어나지 않고
                        x = v[0] + dx[i] 
                        y = v[1]+ dy[i]

                        if x >= 0 and x < m and y >= 0 and y < n:
                            if not visited[y][x] and graph[y][x]: #방문 x, graph에 배추가 있을 때
                                visited[y][x] = True #방문 처리
                                queue.append((x,y)) #좌표 삽입
    print(z_cnt)

T = int(input())
for _ in range(T): #T case
    
    m, n, k = map(int, input().split())
    #가, 세, 배추 위치 개수

    graph = [[False for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(k): #배추 위치 입력
        a, b = map(int, input().split())
        graph[b][a] = True #위치 추가

    bfs(graph, visited, m, n)
