import sys
input=sys.stdin.readline



dp=[0]*101
dp[1]=1
dp[2]=1
dp[3]=1

for _ in range(int(input())):
    n=int(input())
    for x in range(4,n+1):
        dp[x]=dp[x-2]+dp[x-3]
    print(dp[n])