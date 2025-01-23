import sys
input=sys.stdin.readline

def w(a,b,c):
    
    if a<=0 or b<=0 or c<=0:#0보다 작거나 같은 값이면 1을 반환
        return 1
    
    if a>20 or b>20 or c>20: #만약 a,b,c중에 하나라도 20보다 큰 값이 온다면, 20으로세팅
        return w(20,20,20)
    
    #위의 두 조건으로 0부터 20까지의 숫자들로 구성됨을 확인할 수 있다. 
    #일반적인 dp테이블과 다르게 매개변수를 3개 받기 때문에 3차원 리스트로 초기화를 한다.
     
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a<b<c:
        dp[a][b][c]= w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        return dp[a][b][c]
    
    dp[a][b][c]= w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

dp=[[[0]*(21 )for _ in range(21)]for _ in range(21)] #0~20 인 3차원 배열로 초기화를 한다.

while 1:
    a,b,c=map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
    #f'...'는 문자열 안에 변수를 삽입하거나 표현식을 계산한 결과를 바로 넣을 수 있도록 하는 문자열 포매팅 방식이다.
    #{}안에 벼수를 넣으면 해당 변수의 값이 문자열에 삽입된다.