a,b,c,m = map(int, input().split())

cnt_work = 0
cnt_burn = 0

for i in range(24):
    if(m >= cnt_burn+a): 
        cnt_work += b
        cnt_burn += a
    else:
        cnt_burn -= c
        if(cnt_burn < 0):
            cnt_burn = 0
print(cnt_work)