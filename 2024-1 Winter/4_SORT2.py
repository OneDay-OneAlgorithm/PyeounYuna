li = input()

temp = [0]*len(li)
for i, li_value in enumerate(li):
    temp[i] = li_value

temp.sort(reverse=True)

answer = ""
for i in temp:
    answer += str(i)

print(answer)
