def solution(array, commands):
    answer = []
    temp=[]
    a = []
    b = []
    k = []
    for i in range (len(commands)):
        a.append(commands[i][0])
        b.append(commands[i][1])
        k.append(commands[i][2])
        
    for i in range (len(commands)):
        temp = sorted(array[a[i]-1:b[i]])
        answer.append(temp[k[i]-1])
    
    return answer