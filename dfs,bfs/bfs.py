from collections import deque

def bfs(graph, start, visited):
	queue = deque([start])
	visited[start]=True
	while queue:
		v=queue.popleft()
		print(v,end=" ")
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i]=True
    
    
    
graph = [
	[],#0, 노드는 1부터 시작하기 때문에 0번 인덱스틑 공백으로 생성
 	[2,3,8],#1번 노드에 인접한 노드
	[1,7],#2
	[1,4,5],#3
	[3,5],#4
	[3,4],#5
	[7],#6
	[2,6,8],#7
	[1,7]#8
]

visited = [False]*9
bfs(graph,1,visited)
