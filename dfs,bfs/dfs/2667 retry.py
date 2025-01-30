import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().strip())))
arr=[]
z=0
def dfs(x,y):
    global z
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        z+=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(n):
        z=0
        if dfs(i,j)==True:
            arr.append(z)
            result+=1
'''
첫 번째 줄에는 총 단지수를 출력하시요. 
그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한줄에 하나씩 출력하시오
'''
arr.sort()
print(result)
for x in arr:
    print(x)