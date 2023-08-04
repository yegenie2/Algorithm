num = list(map(int, input().split()))
square =[]
for i in range(5):
    square.append(num[i]**2)
print(sum(square)%10)