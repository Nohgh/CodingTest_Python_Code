#투 포인터의 대표 문제
import sys
input=sys.stdin.readline

n=int(input()) #재료의 개수
m=int(input())#갑옷을 만드는데 필요한 수, 목표

l=list(map(int,input().split()))#n개의 재료들이 가진 고유한 번호
l.sort()

start,end=0,len(l)-1
cnt=0
#투 포인터 책의 코드보다
#해당 코다가 더 좋은것 같음
#단순히 start는 처음, end는 끝에서 시작하여
#result합을 계산한다. 그 후 start,end의 번호를 조정, cnt를 증가
while start<end:
    result=l[start]+l[end]
    if result>m:
        end-=1
    elif result<m:
        start+=1
    else:
        cnt +=1
        start+=1
        end -=1
print(cnt)