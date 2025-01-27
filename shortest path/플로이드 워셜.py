#시간복잡도 o(n**3)
#노드의 개수n개-> n번의 단계수행,
#각 단계마다 o(n**2)의 계산 수행
import sys
input=sys.stdin.readline

INF=int(1e9)
n=int(input())
m=int(input())

graph=[[INF] *(n+1) for _ in range(n+1)] #인접행렬 방식

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0 #자기자신 0으로 초기화

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

#점화식: Dab=min(Dab, Dak+Dkb) : A에서 B로 가는 최소 비용과 A에서 K를 거쳐 B로 가는 비용을 비교하여 더 작은 값으로 갱신
#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("0", end=" ")
        else:
            print(graph[a][b],end=" ")
    print()
'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''