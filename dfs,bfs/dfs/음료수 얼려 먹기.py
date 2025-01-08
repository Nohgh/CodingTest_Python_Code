'''
n*m 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

input
n,m이 주어진다
얼음 틀의 형대가 주어진다. (2~n+1줄)

output
한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

'''
# 이 문제는 dfs로 해결할 수 있다. 얼음을 얼릴 수 있는 공간이 상하좌우로 연결되어있다고 표현할 수 있음으로 그래프의 형태로 모델링 할 수 있다.
#특정한 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다
#방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 진행하면, 연결된 모든 지점을 방문할 수 있다.

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input()))) #m개의 줄
    
def dfs(x,y):
    if x <=-1 or x>=n or y <=-1 or y >=m: #주어진 범위를 벗어나는 경우에는 즉시 종료
        return False
    if graph[x][y] == 0 :
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j) ==True:
            result+=1
print(result)
 