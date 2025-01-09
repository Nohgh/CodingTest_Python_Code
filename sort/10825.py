import sys
input=sys.stdin.readline

n=int(input())
list=[]

for _ in range(n):
    a,b,c,d=input().split() #이름, 국어 , 영어, 수학
    list.append((a,int(b),int(c),int(d)))
'''
국어 내림차순 1
국어 같으면 영어 오름차순 2
국어,영어 같으면 수학 내림차순 3
모든 점수 같으면 이름이 사전 순으로 증가하는 순으로(오름차순) 0
'''
list.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for x in list:
    print(x[0])