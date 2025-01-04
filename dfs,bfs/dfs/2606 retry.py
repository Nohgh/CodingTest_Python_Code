import sys
input = sys.stdin.readline
n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
visitCnt=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v]=True
    global visitCnt
    if v != 1:
        visitCnt+=1

    for x in graph[v]:
        if not visited[x]:
            dfs(x)
dfs(1)
print(visitCnt)