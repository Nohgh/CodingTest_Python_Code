arr=[]
arr2=[]
for x in range(1,10000):
    if x < 100: # 1,2자리 수 
        arr.append(x+x//10+x%10)
    elif x <1000: #3자리 수
        arr.append(x + x//100 + (x%100)//10 + (x%100)%10)
    elif x <10000: #4자리 수
        arr.append(x + x//1000 + (x%1000)//100 + ((x%1000)%100)//10 +((x%1000)%100)%10)
    else:
        arr.append(x + x//10000 + (x%10000)//1000 + ((x%10000)%1000)//100 + ((x%10000)%1000)%100 + (((x%10000)%1000)%100)//10 + (((x%10000)%1000)%100)%10)

for x in range(1,10001):
    if x not in arr:
        print(x)