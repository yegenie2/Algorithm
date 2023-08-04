def solution(phone_number):
    answer = phone_number
    for i in range(len(phone_number)-4):
        answer = answer.replace(phone_number[i],'*',1)
    return answer