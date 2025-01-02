import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)#제귀범위 설정

n,m,r = map(int,input().split())
graph = [[] for _ in range (n+1)] #정점은 1부터 있기때문에 0번 인덱스는 비움 

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b) #그래프에 간선 추가
    graph[b].append(a) #서로 추가함 
    
for x in graph:
    x.sort() #인접리스트 내부 정렬

visited=[False] *(n+1) #정점이 1부터 시작하기 때문에 0번인덱스는 비우고 시작

#노드를 방문하고 방문 순서를 출력 , 방문하는 카운트를 전역적으로 관리 필요, 방문 시 증가
cnt=0 

cntArr = [0]* (n+1) #각 정점의 방문순서 저장 배열

def dfs(v):
    global cnt#global로 쓸 변수는 함수 내부에서 정의 
    visited[v]=True
    cnt+=1
    cntArr[v]=cnt
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
dfs(r)

for x in range(1,n+1):
    print(cntArr[x])