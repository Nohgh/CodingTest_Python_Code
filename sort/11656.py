#8분 시작 분 11분 종료
import sys
input=sys.stdin.readline
arr=[]
s=input().strip()
for i in range(len(s)):#baekjoon 8, 0~7
    arr.append(s[i:])
    
arr.sort()
for i in arr:
    print(i)