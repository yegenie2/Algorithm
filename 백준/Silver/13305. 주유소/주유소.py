n = int(input())
length = list(map(int,input().split()))
city =  list(map(int,input().split()))
cnt = 0
m = city[0]

for i in range(n-1):
    if city[i] < m:
        m = city[i]
    cnt += m *length[i]
print(cnt)