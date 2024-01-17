from sys import stdin
stack = []
size = 0
k = int(input())

for _ in range(k):
    command = int(stdin.readline())
    if(command == 0):
        del stack[size-1]
        size -=1
    else:
        stack.append(command)
        size +=1

print(sum(stack))
