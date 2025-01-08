'''
n*m크기의 미로가 있고, 1,1에서 n,m으로 가야한다. 
괴물이 있는 부분은 0, 없는 부분은 1로 표시된다.
탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오

input
n,m
n개의 줄에는 mrodml 정수로 미로의 정보가 주어진다

output
최소 이동 칸의 개수를 출력
'''
#bfs를 이용했을때 효과적으로 해결할 수 있다. bfs는 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문이다.
#1,1지점에서부터 bfs를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다.
#특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더하 값을 리스트에 넣는다. 
#120
#030
#045 이런식으로
from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1] #두 배열의 같은 인덱스가 한 쌍이다.

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):#방향 확인, 현재 위치 기준(x,y)
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx <0 or ny <0 or nx >=n or ny >=m: #미로를 벗어난 경우 무시
                continue
            if graph[nx][ny]==0:#벽인 경우 무시
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]= graph[x][y]+1 #여기서 전 노드의 좌표는 x,y 현재는 그 좌표에서 상하좌우로 움직인 위치
                queue.append((nx,ny))
                
    return graph[n-1][m-1] #가장 오른쪽 아래까지의 최단 거리 반환, 3*3배열에서 제일 끝은 2,2
print(bfs(0,0))