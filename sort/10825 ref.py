#문재 해결 후 발견한 매우 효율적으로 푼 방식
#정렬을 진행하기 전 입력받는 타임에 모두 오름차순으로 정렬될 수 있도록 
#입력을 세팅한다. 
#내 코드보다 조금 더 빠르게 동작하는 코드지만 sort함수 실행시 key값을 
#따로 입력하지 않아도 된다는 장점이 있는 코드.
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
l = []

for i in range(n):
    name,a,b,c = input().split()
    l.append((-int(a),int(b),-int(c),name))

l.sort()

for i in l:
    print(i[3])