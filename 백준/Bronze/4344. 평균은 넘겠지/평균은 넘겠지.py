c = int(input())

for _ in range(c):
    score = []
    avg = 0
    rate = 0
    cnt = 0
    score = list(map(int, input().split()))
    avg = sum(score[1::])/score[0]
    for i in score[1::]:
        if avg<i :
            cnt += 1
    rate = cnt / score[0] *100
    print("{:.3f}".format(round(rate,3))+'%')
