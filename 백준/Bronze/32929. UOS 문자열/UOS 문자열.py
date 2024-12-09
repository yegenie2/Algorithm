n = int(input())
list = ['U', 'O', 'S']
#print(len(list))
addr = n%len(list)
print(list[addr-1])