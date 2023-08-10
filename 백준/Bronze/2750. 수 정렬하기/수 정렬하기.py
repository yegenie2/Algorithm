n = int(input())
num = []
for _ in range(n):
    x = int(input())
    num.append(x)
print(*sorted(num),sep='\n')