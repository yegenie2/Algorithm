chess = [1,1,2,2,2,8]

s = list(map(int, input().split()))
answer = []
for i in range(6):
    answer.append(chess[i]-s[i])
print(*answer)