n = int(input())
arr = []
lst = []
for _ in range(n):
    name = input()
    arr.append(name[0])
for i in arr :
    if arr.count(i) >= 5 : 
        lst.append(i)
        result = "".join(sorted(list(set(lst))))
    elif len(lst) == 0 :
        result = 'PREDAJA'
print(result)