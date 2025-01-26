'''
basic dijkstra algorithm 
시간복잡도 o(v**2) : 총 o(v)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형탐색, 현재 노드와 연결된 노드 매번 일일이 확인 필요
'''
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
    
# print(graph[1][0]) # (2,2)

#방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호를 반환함
def get_smallest_node():
    min_value = INF
    idx=0
    for i in range(1,n+1): #1부터
        if distance[i] < min_value and not visited[i]: #방문하지 않은 요소 중에 최솟값
            min_value =distance[i]
            idx=i
    return idx

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]
    #시작 노드를 제외한 전체 n-1노드에 대해서 반복
    for _ in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node() #방문하지 않은 요소중 거리가 최솟값
        visited[now]=True #방문처리
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]: #방문x 최솟값과 연결된 요소들을 방문
            #만약 방문하지 않은 값이 3이고 이게 5랑 연결되어있다면 1->3->5의 거리를 cost로 저장
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost <distance[j[0]]: #1->5와 1->3->5를 비교
                distance[j[0]]=cost
#다익스트라 알고리즘 수행
dijkstra(start) #1

for i in range(1,n+1):
    #도달할 수 없는 경우 무한이라고 출력
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
'''
6 11
1
1 2 2 
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''