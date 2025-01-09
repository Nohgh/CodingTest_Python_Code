from collections import deque
import sys
input=sys.stdin.readline
#노드의 부모를 찾는 방법 = 현재 노드를 탐색하기 전 노드를 visited에 기록한다.
#bfs로 풀어보기 
n=int(input())

graph=[[]for _ in range(n+1)]
parent=[0]*(n+1)
visited=[False]*(n+1)

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(v):
    q=deque([v])
    visited[v]=True
    while q:
        x=q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
                parent[i]=x
bfs(1)
for i in range(2,n+1):
    print(parent[i])