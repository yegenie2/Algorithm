a,b = map(int,input().split())

c = int(input())

m_sum = b+c
if m_sum < 60 :
    minute = m_sum
    hour = a
else : 
    if m_sum % 60 == 0 :
        time_h = m_sum // 60
        hour = a + time_h
        minute = m_sum % 60
        if hour >= 24: 
            hour = hour%24
    else : 
        minute = m_sum % 60
        time_h = m_sum // 60
        hour = a + time_h
        if hour >= 24: 
            hour = hour%24
print (hour, minute)