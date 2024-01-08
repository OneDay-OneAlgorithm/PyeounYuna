n, m = map(int, input().split())
n_li = list(map(int, input().split()))
n_li.sort()
ans = []

def back():
    for i in n_li:
        if len(ans) == m:
            print(" ".join(map(str, ans)))
            return
        ans.append(i) #추가하고
        back() #경우의 수 탐색하고
        ans.pop() #리턴되면 값 하나 빼고
back()