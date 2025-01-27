import heapq
import sys
input=sys.stdin.readline

INF=int(1e9) #10억, 무한 , 실수->정수

n=int(input())
m=int(input())

graph=[[]for _ in range(n+1)]

visited = [False]*(n+1)

distance = [INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))	#a-(c:가중치)->b
    
start,end=map(int,input().split())

def dijkstra(start):
    q=[] #heapq
    heapq.heappush(q,(0,start)) #힙에 들어가는 요소: (거리,노드)
    distance[start]=0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q) 
        if distance[now] <dist:
            continue
        for i in graph[now]:#최단 거리로 갱신되었다면 실행, 꺼낸 요소와 연결된 노드 순회
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    
dijkstra(start)
print(distance[end])
