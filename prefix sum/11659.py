import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

def prefix_sum(n):
    prefixSum=[0]*n
    prefixSum[0]=arr[0]
    for i in range(1,n):
        prefixSum[i]=prefixSum[i-1]+arr[i]
    return prefixSum

prefixSum=prefix_sum(n)
rst=[]
for _ in range(m):#범위에 따라 리턴 달리해야함
    i,j=map(int,input().split())
    if i==1 and j!=1:
        rst.append(prefixSum[j-1])
    elif i==j:
        rst.append(arr[j-1])
    else:
        rst.append(prefixSum[j-1]-prefixSum[i-2])
        
for x in rst:
    print(x)