#전자레인지
import sys
input = sys.stdin.readline
s=int(input())

if s %10 !=0:
    print(-1)
else:
    for x in [300,60,10]:
        if s >= x:
            print(s//x,end=' ')
            s%=x
        else:
            print(0,end=' ')
        
