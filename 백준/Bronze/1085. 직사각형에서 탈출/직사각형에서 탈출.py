min_len=[]
x,y,w,h = map(int,input().split())

min_len.append(abs(0-x))
min_len.append(abs(0-y))
min_len.append(abs(w-x))
min_len.append(abs(h-y))

print(min(min_len))