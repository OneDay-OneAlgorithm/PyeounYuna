N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
ans = []

def solve():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != L[i]:
            visited[i] = True
            ans.append(L[i])
            overlap = L[i]
            solve()
            visited[i] = False
            ans.pop()

solve()