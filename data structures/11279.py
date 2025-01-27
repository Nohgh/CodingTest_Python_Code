import heapq
import sys
input=sys.stdin.readline

q=[]
n=int(input())
for _ in range(n):
    x=int(input())
    if x==0:
        if len(q)==0: #배열이 비어있는데 가장 큰 값을 출력하라고 한 경우
            print(0)
        else:
            z=-heapq.heappop(q)
            print(z)
            # print("제거한 이후의 q",q)
    else:
        heapq.heappush(q,-x)