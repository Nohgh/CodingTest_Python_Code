
while(1):
    n=int(input())
    if n==-1: break
    sum=0
    arr=[]
    for x in range(1,n):
        if n%x==0: arr.append(x)
    for x in arr:
        sum+=x
    if sum==n:
        print(n,end=" = ")
        print(' + '.join(map(str,arr)))
    else:
        print("%d is NOT perfect." %n)