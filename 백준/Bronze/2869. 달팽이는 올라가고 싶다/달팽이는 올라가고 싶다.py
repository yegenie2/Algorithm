import sys
import math
a,b,v = map(int, sys.stdin.readline().split())
day = (v-b)/(a-b)   
print(math.ceil(day)) # 소수점 발생시 올림함수 써서 day+1 해줌.