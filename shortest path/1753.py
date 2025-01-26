'''
better dijkstra algorithm 
'''
import heapq
import sys
input=sys.stdin.readline

INF=int(1e9) #10억, 무한 , 실수->정수

#노드의 개수, 간선의 개수 입력
n,m=map(int,input().split())

#시작 노드 번호 입력
start = int(input())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 
graph=[[]for _ in range(n+1)]

#방문 여부 체크 리스트
visited = [False]*(n+1)

#최단거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))	#a-(c:가중치)->b
    

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
    
#다익스트라 알고리즘 수행
dijkstra(start) #1

for i in range(1,n+1):
    #도달할 수 없는 경우 무한이라고 출력
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])
