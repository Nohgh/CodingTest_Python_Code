import sys
import heapq
input=sys.stdin.readline

n=int(input())
minus=[]
plus=[]
for _ in range(n):
    x=int(input())

	#0이라면 배열에서 절댓값이 가장 작은 값을 출력, 배열에서 제거
    if x==0:
        plusLen=len(plus) #양수배열길이
        minusLen=len(minus)
        if plusLen==0 and minusLen==0:#모두 비어있는 경우 0 출력
            print(0)
            continue
        if plusLen==0 and minusLen!=0: #양수 없고 음수에만 값이 있는 경우 
            z=-heapq.heappop(minus)
            print(z)
            continue
        if minusLen==0 and plusLen!=0:
            z=heapq.heappop(plus)
            print(z)
            continue
        plusItem=plus[0]
        minusItem=minus[0]
        if plusItem<minusItem:
            z=heapq.heappop(plus)
            print(z)
        else:#minusItem이 더 크거나 같은경우
            z=-heapq.heappop(minus)
            print(z)

    elif x>0:
        heapq.heappush(plus,x)
    else:
        heapq.heappush(minus,-x) #-1입력시, 1 저장