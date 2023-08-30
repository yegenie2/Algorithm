l, p = map(int, input().split())
news = list(map(int, input().split()))
result = l*p
for i in range(len(news)) :
    news[i] = news[i] - result
print(*news)