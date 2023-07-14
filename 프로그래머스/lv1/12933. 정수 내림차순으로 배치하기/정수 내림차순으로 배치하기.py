def solution(n):
    num = int(n)
    
    num_list = list(str(num))
    num_list.sort(reverse= True)

    return int(''.join(num_list))