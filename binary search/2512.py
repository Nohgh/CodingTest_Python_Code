import sys #이분탐색의 문제는 입력되는 범위가 크기때문에 반드시 input을 sys.stdin.readline으로 정의하기 
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
m=int(input())

rst,s,e=0,1,max(arr)

while s<=e:
    sum=0
    mid=(s+e)//2
    for i in arr:
        if i<mid:
            sum+=i
        else:
            sum+=mid
    if sum<=m:#작거나 같은 경우는 rst를 초기화, mid를 높여 합이 더 커지게 함
        rst=mid
        s=mid+1
    else: 
        e=mid-1 #sum이 m보다 크다면, 작거나 같은 경우가 될떄까지 단순히 끝점을 초기화
print(rst)