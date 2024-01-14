from sys import stdin
T = int(input())
ip = []

for _ in range(T):
    ip = stdin.readline()
    size = 0
    stack = []
    check = 0
    for i in range(len(ip)):
        if(ip[i] == '('): #push
            stack.append(1)
            size +=1

        if(ip[i] == ')'): #pop
            if(size == 0):
                check = 1
                break
            else:
                del stack[size-1]
                size -=1

    if(check == 0 and size==0):
        print("YES")
    else:
        print("NO")