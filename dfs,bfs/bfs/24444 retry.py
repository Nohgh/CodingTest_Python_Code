import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,r= map(int,input().split())
graph= [[] for _ in range(n+1)] #인접리스트
visited= [False]*(n+1)
cnt= 0
cntArr=[0]*(n+1)

for _ in range(m):
	a,b = map(int,input().split()) 
	graph[a].append(b)
	graph[b].append(a)
	
for x in graph:
	x.sort() #문제에서 오름차순 요청

def bfs(r):
	global cnt
	queue=deque([r])
	visited[r]=True
	cnt+=1
	cntArr[r]=cnt
	while queue:
		v=queue.popleft()
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i]=True
				cnt+=1
				cntArr[i]=cnt
bfs(r)
for x in range(1,n+1):
	print(cntArr[x])