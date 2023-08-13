answer =[]
temp=[]
for i in range(5):
    num = int(input())
    answer.append(num)
temp = sorted(answer)
print(int(sum(answer)/len(answer)))
print(temp[len(temp)//2])