h, m, s = map(int, input().split())
time = int(input())

s_sum = s + time
if s_sum < 60 :
    s = s_sum
if s_sum >= 60 :
    m = m + (s_sum//60)
    s = s_sum % 60
if m >= 60 :
    h = h + (m//60)
    m = m % 60
if h >= 24 :
    h = h % 24
print(h,m,s)