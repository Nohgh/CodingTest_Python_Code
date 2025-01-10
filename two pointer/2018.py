import sys
input=sys.stdin.readline
n=int(input())
# l=[i for i in range(1,int(input())+1)]
sum=0
end=1
cnt=0
for start in range(1,n+1):
    while sum < n and end <= n:
        sum+=end
        end+=1
    if sum == n:
        cnt+=1
    sum-=start
print(cnt)
