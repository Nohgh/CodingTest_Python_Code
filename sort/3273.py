# import sys
# input=sys.stdin.readline

# n=int(input())
# arr=list(map(int,input().split()))
# x=int(input())
# '''
# 일단 arr을 정렬
# 정렬된 arr에서 for문으로 순회를 i로 두고 함
# i와 합쳐서 x가 될 숫자를 arr에서 탐색

# '''
arr=[]
for i in range(1,30):
    arr.append(i)
print(sum(arr))
print(arr)