from collections import deque

n,k=map(int,input().split())

max_num=100000 #움질일 수 있는 최대 좌표를 설정
visited=[0]*(max_num+1) #최대 좌표만큼 모두 0으로 초기화

def bfs(): #dfs보다는 bfs가 적합
    q=deque()
    q.append(n)
    while q:
        x= q.popleft()
        if x==k:
            print(visited[x])
            break
        for i in (x-1, x+1, x*2): #이동할 수 있는 방향 
            if 0 <=i<=max_num and not visited[i]: #주어진 범위 내에 있고, 아직 방문하지 않았다면면
                #배열의 요소가 0인 경우에는 not 원소를 하면 true를 반환한다.
                visited[i]=visited[x]+1 #이동한 위치에 현재 이동한 시간을 표시, 전 좌표의 시간에 +1 한다.
                q.append(i)
bfs()