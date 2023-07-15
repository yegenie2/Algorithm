def solution(x):
    num = sum([int (i) for i in str(x)])
    if x % num == 0:
        return True
    else :
        return False