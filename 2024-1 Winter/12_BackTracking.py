n, m = map(int, input().split())
ans = []
n_li = list(map(int, input().split()))
n_li.sort()

def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    for i in n_li:
        if not i in ans:
            ans.append(i)
            back()
            ans.pop()
back()