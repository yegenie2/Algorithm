
def solution(arr):
    answer = [arr[0]]
    for i in range(len(arr)):
        if answer[-1] != arr[i]:        # list[-1]는 리스트의 맨 마지막 요소
            answer.append(arr[i])
    return answer