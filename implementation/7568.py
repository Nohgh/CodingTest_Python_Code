import sys
input = sys.stdin.readline

arr=[]

for _ in range(int(input())):
    a,b = map(int,input().split())
    arr.append((a,b))
rst=list(1 for _ in range(len(arr)))

for x in range(len(arr)):
    for y in range(len(arr)):
        if x != y :
            if arr[x][0]<arr[y][0] and arr[x][1]<arr[y][1]:
                rst[x]+=1 #등수 증가
print(*rst)
#한번에 딱 깔끔쓰 하게 품 ㄴㅇㅅ