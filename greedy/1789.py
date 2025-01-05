import sys
input=sys.stdin.readline

sum=0
cnt=0
s=int(input())
for i in range(1,s+1):
    sum+=i
    cnt+=1
    if sum > s:
        break
print(cnt-1)