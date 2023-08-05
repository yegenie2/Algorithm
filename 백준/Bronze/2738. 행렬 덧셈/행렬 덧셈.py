n, m  = map(int, input().split())

answer = []
x_matrix = []
y_matrix = []

for _ in range(n):
    x = list(map(int,input().split()))
    x_matrix.append(x)

for _ in range(n):
    y = list(map(int, input().split()))
    y_matrix.append(y)

for i in range(n):
    row_sum = []
    for j in range(m):
      row_sum.append(x_matrix[i][j] + y_matrix[i][j])
    answer.append(row_sum)

for row in answer:
    print(' '.join(map(str, row)))