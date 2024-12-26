import sys
input = sys.stdin.readline

n=int(input())
arr=[]
cnt=0

for _ in range(n):
    arr.append(int(input()))
num1 = arr[0]
if n==1:
    cnt=0
    print(0)
else:
    newArr = arr[1:] #비교 위한 베열

    while(True):
        newArr.sort(reverse=True)
        if(num1>newArr[0]):
            break
        else:
            newArr[0]-=1
            num1+=1
            cnt+=1

    print(cnt)