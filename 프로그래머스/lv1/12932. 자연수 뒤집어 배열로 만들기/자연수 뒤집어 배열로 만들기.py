def solution(n):
    answer = []
    answer = list(str(n))
    answer.reverse()
    
    return list(map(int,answer))
            