#시간복잡도 o(n**2)의 코드

def prefix_sum(n,m):
    prefixSum=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            prefixSum[i][j]=prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]+arr[i-1][j-1]
    return prefixSum
    
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
prefixSum=prefix_sum(n,m)
print(prefixSum)

#(i,j)에서 (x,y)까지의 부분합을 구하는 , o(1)의 코드
i,j,i2,y2=map(int,input().split())
partSum=prefixSum[i2][y2]-prefixSum[i-1][y2]-prefixSum[i2][j-1]+prefixSum[i-1][j-1]
print(partSum)