'''
x가 주어질 때 정수 x에 사용할 수 있는 연산
1. x가 5로 나누어 떨어지면 5로 나눈다
2. x가 3으로 나누어 떨어지면 3으로 나눈다.
3. x가 2로 나누어 떨어지면 2로 나눈다.

26-> 25-> 5->1

입력: x, (1<=ㅌ<=300000)
출력: 연산을 하는 횟수의 최솟값
'''

'''
도식화
6
5    3    2
4,1  2,1  1,1
즉 같은 함수 동일하게 호출되는거 확인

문제에서 요구한 내용 점화식 표현->
a(i)=min(a(i-1), a(i/2), a(i/3), a(i/5))+1

1을 빼는연산을 제외하고는 해당 수로 나누어떨어지는 경우에만 점화식을 사용할 수있다(조건만족시)

'''
x=int(input())
d=[0]*30001 #1의 경우에는 계산할필요가 없으므로 0으로 세팅

for i in range(2,x+1):
    
    d[i]=d[i-1]+1 #d[i]는 i를 1로 만들기 위한 최솟값
    
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1) #2,3,4,...x까지 각각의 최소연산을 d리스트에 저장
        
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
        
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
print(d[x])