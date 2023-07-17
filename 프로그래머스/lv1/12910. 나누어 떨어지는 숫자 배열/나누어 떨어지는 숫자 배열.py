def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:            # answer의 길이가 0이면 나누어 떨어지는 숫자들이 없다는 뜻.
        return [-1]
    answer.sort()
    return answer