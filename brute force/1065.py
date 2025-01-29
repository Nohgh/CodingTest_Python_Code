import sys
input=sys.stdin.readline

n=int(input())
cnt=0
for x in range(1,n+1):
    if x<100:
        cnt+=1
    #78 76 88 80
    #11 22 33 44 55 66 77 88 99
    
    #100 101 102 103 104 105 106 107 108 109 110
    #100이상-> 102 1개 
    #321, 123, 246, 642이런게 한수
    elif x<1000:
        x=str(x)
        d1=int(x[0])-int(x[1])
        d2=int(x[1])-int(x[2])
        if d1==d2:
            cnt+=1
print(cnt)