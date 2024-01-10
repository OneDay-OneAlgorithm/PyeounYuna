import sys
import heapq
input = sys.stdin.readline
 
N = int(input())
arr = []

#입력
for _ in range(N):
    arr.append(list(map(int, input().split())))

#회의시간 기준 정렬
arr.sort(key=lambda x: x[0])
 
rooms = [0]
answer = 1

for s, e in arr:
    # 가장 빠른 회의 종료 시간보다 array의 회의 시작 시간이 늦거나 같다면
    if s >= rooms[0]:
        # 그 회의 시간을 pop해준 다음 새로운 종료 시간 삽입
        heapq.heappop(rooms)

    else:
        # 가장 빠른 회의 종료 시간보다 빠르다면 회의실 추가 후 종료 시간 삽입
        answer+=1

    # 삽입부 : 이렇게 하면 여러 개를 관리할 수 있음
    heapq.heappush(rooms, e)
 
print(answer)