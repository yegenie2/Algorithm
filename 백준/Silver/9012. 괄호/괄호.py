t = int(input())

for i in range(t):
    lst = []
    s = input()
    for j in s:
        if j == '(':
            lst.append(j)

        if j == ')':
            if len(lst) != 0:
                lst.pop()
            else:
                lst.append(j)
                break
            
    if len(lst) == 0:
        print("YES")
    else:
        print("NO")