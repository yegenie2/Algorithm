def solution(array):
    answer = []
    tmp = max(array)
    answer.append(tmp)
    for i in range(0,len(array)):
        if array[i] == tmp:
            answer.append(i)
    return answer