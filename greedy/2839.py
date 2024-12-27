import sys
input = sys.stdin.readline

cnt=0
n=int(input()) 

while(n%5!=0):
    if n<3:
        cnt=-1
        break 
    n-=3 
    cnt+=1 
if cnt!=-1:
    cnt+= n//5 
    print(cnt)
else:
    print(-1)
    