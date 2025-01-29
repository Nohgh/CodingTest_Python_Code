def prefix_sum(n):
    prefixSum=[0]*n
    prefixSum[0]=arr[0]
    for i in range(1,n):
        prefixSum[i]=prefixSum[i-1]+arr[i]
    return prefixSum

n=int(input())
arr=list(map(int,input().split()))
prefixSum=prefix_sum(n)
print(prefixSum)