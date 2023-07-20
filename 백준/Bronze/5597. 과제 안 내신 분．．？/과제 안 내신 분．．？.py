import itertools

student = [x for x in range(1,31)]
homework = []
no_homework = []
for i in range (28):
    num = int(input())
    homework.append(num)
        
no_homework.append(list(set(student)-set(homework)))    #차집합으로 빼줌
no_homework = list(itertools.chain(*no_homework))    #2차원 배열로 들어가서 다시 1차원 배열로 바꿔줌
no_homework.sort()
print(no_homework[0])
print(no_homework[1])