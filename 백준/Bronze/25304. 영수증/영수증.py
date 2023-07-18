x = int(input())    #총금액
n = int(input())    # 물건의 종류의 수
sum_price = 0
for i in range(n):
    a,b = map(int,input().split())
    price = a*b
    sum_price += price
if x == sum_price :
    print('Yes')
else :
    print('No')