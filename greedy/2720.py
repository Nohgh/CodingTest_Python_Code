'''
왜 그리디인가
-> 큰 단위의 동전을 먼저 거슬러서 사용자에게 최소의 동전을 줄 수 있도록 한다.
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a=25
    b=10
    c=5
    d=1
    
    numA = n//a
    n=n%a
    
    numB = n//b
    n=n%b
    
    numC = n//c
    n%=c
    
    numD = n//d
    n%=d
    
    print(numA,numB,numC,numD)

    
    