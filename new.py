import sys
input=sys.stdin.readline

#정점의 수, 간선의 수, 시작 정점
n,m,r=map(int,input().split()) 

graph=[[]for _ in range(n+1)]
#m개 줄에 간선 u v
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for x in graph: #인접정점은 오름차순으로 방문
    x.sort()
visitied=[False]*(n+1)

#방문순서 기록
cnt=0 #계속 증가
#각 정점의 개수만큼 cnt를 기록할 배열 생성, 0으로 초기화-> 업데이트
cntArr=[0]*(n+1)

def dfs(v):
    global cnt #cnt변수를 global로 선언
    visitied[v]=True
    cnt+=1
    cntArr[v]=cnt
    for i in graph[v]:
        if not visitied[i]:
            dfs(i)
dfs(r)

for x in range(1,n+1):
    print(cntArr[x])