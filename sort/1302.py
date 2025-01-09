#44분 시작 56분 종료
import sys
input=sys.stdin.readline
# 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 
# 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
d=dict()
for _ in range(int(input())):
    s=input().strip()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
        
d=sorted(d.items(), key=lambda x:(-x[1],x[0])) 
#딕셔너리 같은 경우에는 sorted로 정렬, #items를 첫 매개변수로 주고, 두번째 매개변수에서 람다를 정의
print(d[0][0])
#56