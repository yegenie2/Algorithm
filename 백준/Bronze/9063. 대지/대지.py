count = int(input())
arr_x =[]
arr_y = []
for i in range (count):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

x_length = max(arr_x)-min(arr_x)
y_length = max(arr_y)-min(arr_y)
print(x_length * y_length)