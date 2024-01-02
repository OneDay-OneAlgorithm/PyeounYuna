# 그리디 문제 2
from sys import stdin

N = int(stdin.readline())
li = [] #start, end, time
cnt = 0
max = 0
update = 0
#회의 시간, 인덱스

for i in range(N):
    li.append(list(map(int, stdin.readline().split()))) #start, end
    # li[i].append(li[i][1] - li[i][0]) #회의 시간
    if(li[i][1] > max): max = li[i][1]

status = [0]*(max+1)
#회의 종료 시각 기준 정렬
li.sort(key=lambda li:li[1])
#동일한 종료 시각 중, 빠른 시작 시간 기준 정렬

index_start = -1
index_end = -1

for i in range(N-1):
    #만약, 끝나는 시간이 같고
    if(li[i][1] == li[i+1][1]):
        if(index_start == -1 ):
            index_start = i
            index_end = i+1
        else:
            index_end = i+1
    elif(index_start != -1):
        li[index_start:index_end+1] = sorted(li[index_start:index_end+1])
        index_start = -1
        index_end = -1

if(index_start != -1):
    li[index_start:index_end+1] = sorted(li[index_start:index_end+1])

for start, end in li:
    if(start >= update):
        cnt += 1
        update = end
    
print(cnt)
