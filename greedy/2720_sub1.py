'''
참고한 풀이
동전의 단위를 배열로 할당,
배열을 순회하며 단순히 목을 출력하고 나머지를 거스름돈으로 갱신

반복문으로 단순 반복을 제거
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    for x in [25,10,5,1]:
        print(n//x, end=' ')
        n=n%x        