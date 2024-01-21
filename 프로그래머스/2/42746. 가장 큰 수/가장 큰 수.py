def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*3, reverse=True)
    answer = answer.join(numbers)
    return str(int(answer))     #str -> int -> str 이유는 000인 경우 0으로 만들기 위해