#배열, 시작, 끝
def quick_sort(array, start, end):

    #만약 시작이 끝보다 크다면
    if start >= end:
        return
    
    #호어 퀵소트이므로 시작을 피벗으로 설정
    pivot = start
    left = start + 1
    right = end

    #left값 index가 end값보다 같거나 작은 상태에서 left가 피벗보다 작다면
    #left는 피벗보다 큰 값을 찾을 때까지 반복해야함
    while left <= end and array[left] <= array[pivot]:
        left += 1
    
    #right값 index가 start값보다 큰 상태에서 피벗보다 크다면
    #right의 목표는 피벗보다 작아야함
    while right > start and array[right] >= array[pivot]:
        right -= 1

    #만약 둘이 엇갈렸다면 스왑
    if left > right:
        array[right], array[pivot] = array[pivot], array[right] 
    else:
        array[left], array[right] = array[right], array[left]
    
    #범위를 줄여나가며 재귀적으로 반복
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)

# 배열의 크기, 교환 횟수
n = int(input())
array = []
for i in range(n):
    a = int(input())
    array.append(a)

quick_sort(array, 0, len(array) -1)

for i in range(n):
    print(array[i])