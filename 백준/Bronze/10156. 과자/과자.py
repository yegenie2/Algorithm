k,n,m = map(int, input().split())
money = k*n
if money > m:
    print((k*n)-m)
else:
    print(0)