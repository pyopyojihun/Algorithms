#완전탐색유형 그리디 알고리즘 백준 문제 
import time
import sys


n,m=map(int,sys.stdin.readline().split())
total=0
remainder=0
list=[]
for i in range(n):
    list.append(int(input()))
start_time=time.time()#측정시작
list.reverse()
for j in range(0,len(list)):
        if m>=list[j]:
            total=total+m//list[j]
            remainder=m%list[j]
            m=m%list[j]
        if m==0:
             break    

print(total)

end_time=time.time()#측정종료

print("time: ", end_time-start_time)
