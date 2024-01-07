from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1,n+1)])
ans = []
maker = k-1

for i in range(n):
    ans.append(queue[maker])
    queue.remove(queue[maker])
    if len(queue) !=0:
        maker = (maker + k-1)%len(queue)

print("<"+", ".join(map(str,ans))+">")