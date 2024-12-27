import sys
input = sys.stdin.readline

pay=int(input())
n=1000-pay 
cnt =0
for x in [500,100,50,10,5,1]: 
    
    if n>=x: #범위 설정시 정확히 나누어 떨어지는 경우도 고려하여 크거나 같은 경우로 수정
        cnt+=n//x
        n=n%x
    
print(cnt)