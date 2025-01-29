import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]


def prefix_sum(n,m):
    prefixSum=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            prefixSum[i][j]=prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]+arr[i-1][j-1]
    return prefixSum
        
prefixSum=prefix_sum(n,n) #여기서 매개변수 m자리에 m을 전달하면 안됨
# print(prefixSum)
rst=[]
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
  
    partSum=prefixSum[x2][y2]-prefixSum[x1-1][y2]-prefixSum[x2][y1-1]+prefixSum[x1-1][y1-1]
    rst.append(partSum)
    
for x in rst:
    print(x)