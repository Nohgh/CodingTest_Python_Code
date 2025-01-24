import sys
input=sys.stdin.readline

arr=[]
n=int(input())
for _ in range(n):
    arr.append(list(map(int,input().split())))
#j로 접근하라  
for i in range (1,n):
    for j in range(i+1):
        if j==0:
            arr[i][j]+=arr[i-1][j] #위에서 현재값을 더해주는 로직 
        elif j==len(arr[i])-1:
             arr[i][j]+=arr[i-1][j-1]
        else:
            arr[i][j]+=max(arr[i-1][j-1],arr[i-1][j])
    
                
        
print(max(arr[n-1]))

#기존의 내 로직은 현재값에서 아래 행의 값을 정의,
#참고한 로직은 현재값을 위의 행에서 가져와 정의