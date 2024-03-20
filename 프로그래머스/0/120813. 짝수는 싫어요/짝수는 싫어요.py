def solution(n):
    answer = []
    odd = 0
    for i in range(1,n+1):
        odd = (2*i)-1
        if odd >n:
            break
        answer.append(odd)
        
        
        
        
    return answer