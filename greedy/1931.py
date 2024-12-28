import sys
input = sys.stdin.readline

meeting=[]
fix=[]

#회의실 배정
for _ in range(int(input())):
    start,end = map(int,input().split(' '))
    meeting.append([start,end])
    
meeting = sorted(meeting, key=lambda x: (x[1],x[0]))  
#lambda 기준을 2개로 설정, 
#1번: 1번째 값
#2번: 0번째 값
for x in meeting:
    if len(fix)==0:
        fix.append(x)
        continue
    if x[0]>=fix[-1][1] and x[1]>=fix[-1][1]:
        fix.append(x)
print(len(fix))
