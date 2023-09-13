word = input().upper()
dic = {}
for i in word:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1

max_list = [k for k , v in dic.items() if v == max(dic.values())]  #max 여러개 일 경우 리스트컴프리핸션
if len(max_list) > 1:
    print("?")
else :
    print(*max_list)
