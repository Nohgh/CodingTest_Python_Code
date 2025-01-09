import sys
input=sys.stdin.readline
from collections import deque
n=int(input())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

limit=0
dx=[-1,1,0,0]
dy=[0,0,1,-1]
cnt=0
rst=[]

def bfs(a,b,limit):
    global cnt
    cnt=0
    q=deque()
    q.append((a,b))
    graph[a][b]=0
    cnt+=1
    print(limit,cnt)
    #한 점이 limit보다 놓은 지점들로만 bfs할 수 있도록 하기 
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if graph[nx][ny]>limit:
                q.append((nx,ny))
                graph[nx][ny]=0
                cnt+=1
    return cnt
for x in range(1,n+1):
    limit=x
    rst.append(bfs(0,0,limit))
print(rst)