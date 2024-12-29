import sys
input=sys.stdin.readline

n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr1.sort()
arr2.sort(reverse=True)
s=0
for x in range(n):
    s+=arr1[x]*arr2[x]
print(s)
    