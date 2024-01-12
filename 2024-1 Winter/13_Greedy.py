n = int(input())
p = list(map(int, input().split()))

#정렬
p.sort()

total = 0
sum = 0

for i in p:
    sum += i
    total += sum

print(total)