import sys
input=sys.stdin.readline
n=int(input())
l=1
dp=[1]*n
arr=list(map(int,input().split()))
for i in range(n):
    if i==n-1:
        break
    if arr[i]<arr[i+1]:
        l+=1
print(l)