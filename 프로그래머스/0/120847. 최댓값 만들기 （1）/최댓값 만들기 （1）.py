def solution(numbers):
    answer = 0
    numbers.sort()
    n = len(numbers)
    answer = numbers[n-2]*numbers[n-1]
    return answer