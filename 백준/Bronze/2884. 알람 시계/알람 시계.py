h,m = map(int,input().split())

if m <45:
    x = abs(m-45)
    m_alarm = 60-x
    if h ==0:
        h_alarm = 23-h
    else:
        h_alarm = h-1
else:
    m_alarm = m-45
    h_alarm = h

print (h_alarm, m_alarm)