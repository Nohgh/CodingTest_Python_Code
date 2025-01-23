import sys
input=sys.stdin.readline

n=int(input())

dp=[0]*1000001

dp[1]=1
dp[2]=2

for x in range(3,n+1):
	dp[x]=(dp[x-1]+dp[x-2])%15746
		
print(dp[n])
# mod부분을 dp를 print하는 과정에서 나누게 되면 리스트의 범위가 백만이나 되기 떄문에 메모리 초과가 발생한다.