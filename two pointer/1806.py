import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(map(int,input().split()))

count=0
interval_sum=0
end=0

min=999999999999

for start in range(n):
    
    while interval_sum < m and end < n:
        interval_sum+=data[end]
        end+=1
        
    if interval_sum >= m:
        count+=1
        
        if (end-start)<min:
            min=end-start
            
    interval_sum-=data[start]
    
    
if min ==  999999999999:
    print(0)
    
else:  
	print(min)
 
#문제에 보면 누적합이 m과 동일이 아니라 크거나 같은 경우임,,,
#따라서 intervaer_sum과 m의 대소를 비교할떄 크거나 같은 경우로 작성하면 됨 