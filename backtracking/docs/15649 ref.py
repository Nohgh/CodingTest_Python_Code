import sys
input=sys.stdin.readline

n,m=map(int,input().split())
array=[]
#1부터 n까지 자연수 주에서 중복없이 m개를 고른 수열
#4 4 
# 1,2,3,4가지고 숫자 4개를 중복 없이 선택

def backtracking():
    if len(array)==m:
        print(" ".join(map(str,array)))
        return
    for i in range(1,n+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()
backtracking()