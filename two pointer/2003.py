import sys
input=sys.stdin.readline

n,m=map(int,input().split()) #m이 되는 경우의 수 구하기
l=list(map(int,input().split()))

count=0
sum=0
end=0

for start in range(n):
    while sum<m and end<n:
        sum+=l[end]
        end+=1
    if sum == m :
        count+=1
    sum-=l[start]
print(count)
#이 문제는 또 start와 end를 맨 뒤에 배치해서 값을 더하는 방식으로만 해결 불가
#투 포인터 문제는 문제의 요청에 따라서 다르게 코드를 바꿔가며 풀어야하는 듯