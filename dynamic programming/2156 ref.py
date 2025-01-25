import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int((input())))

dp=[0]*(n)

#6, 10, 13, 9, 8, 1
#6 10 9 8 16+9 = 25
for i in range(n):
    if i==0:
        dp[0]=arr[0]
    elif i==1:
        dp[1]=arr[0]+arr[1]
    elif i==2:
        dp[2]=max(arr[0]+arr[1],arr[0]+arr[2],arr[1]+arr[2])
    else:
        # 기존 내 코드 : dp[i]= max( dp[i-3]+arr[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1] ) 
        # #-> 여기서 dp[i-2]를 추가하고, dp[i-3]+arr[i-2]+arr[i]이거는 dp[i-2]+arr[i]로 바꿈
        #현재 i를 선택하지 않고 i-1의 dp를 선택하는 경우도 있음
    
        dp[i]=max(dp[i-3]+arr[i-1]+arr[i], dp[i-1], dp[i-2]+arr[i])

print(max(dp))