a = int(input())
b = int(input())
c = int(input())

answer = []
count_answer=[0]*10
for i in str(a*b*c):
    answer.append(i)
for i in answer:
    count_answer[int(i)] += 1
print(*count_answer,sep='\n')