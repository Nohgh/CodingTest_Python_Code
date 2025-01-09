import sys
input=sys.stdin.readline

n=int(input())
list=[]

for _ in range(n):
    a,b,c,d=input().split() #이름, 국어 , 영어, 수학
    list.append((a,int(b),int(c),int(d)))
'''
국어 내림차순
국어 같으면 영어 오름차순
국어,영어 같으면 수학 내림차순
모든 점수 같으면 이름이 사전 순으로 증가하는 순으로(오름차순)
'''
