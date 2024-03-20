def solution(array):
    answer = 0
    tmp = 0
    array.sort()
    if len(array) % 2 != 0:
        tmp = len(array)//2
        answer = array[tmp]
        
    return answer