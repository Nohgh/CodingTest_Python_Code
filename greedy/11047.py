import sys
input = sys.stdin.readline

a,n = map(int,input().split())
arr=[]
cnt=0

for _ in range(a):
    arr.append(int(input()))

# 다른 사람의 풀이에서 이미 정렬된 상태로 입력이 오기때문에
# sort를 하지 않고 
# reversed(arr)로 해결하는 경우도 있었음
# 이 경우 정렬에 대한 시간을 절약할 수 있는 방법으로 평가됨
for x in reversed(arr):
    if n >= x:
        cnt+=n//x
        n%=x
print(cnt)

    