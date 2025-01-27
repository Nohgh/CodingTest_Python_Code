import sys
input=sys.stdin.readline

INF=int(1e9)
n=int(input())
m=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b,c= map(int,input().split())
    #여기가 킥, 문제의 조건처럼  3 4 1 / 4 3 2 와 같이 노선이 여러개인 경우, 최솟값으로 세팅
    if graph[a][b]!=INF:
        graph[a][b]=min(graph[a][b],c) 
    else:
    	graph[a][b]=c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("0",end=" ")
        else:
            print(graph[a][b],end=" ")
    print()