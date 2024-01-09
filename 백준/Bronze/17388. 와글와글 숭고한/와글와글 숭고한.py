num = list(map(int, input().split()))

if sum(num) >= 100 :
    print("OK")
else :
    min(num)
    if min(num) == num[0]:
        print("Soongsil")
    elif min(num) == num[1]:
        print("Korea")
    elif min(num) == num[2]:
        print("Hanyang")