#플레 문제 도전!!
#큰 수 만들기 
arr=['3','301','31','32','3001','333','322','22222','22','111','1'] # 지금 앞에있던 큰 수들은 다 때어낸 상태 
#3 32 31 301
arr.sort(reverse=True)
print(arr)
# for x in range(len(arr)):
#     print(arr[x][0])


# ['333', '322', '32', '31', '301', '3001', '3', '22222', '22', '111', '1']
p=0
str=""
while arr:
    if len(arr)==1:
        str+=arr[p]
        
    case1=int(arr[p]+arr[p+1])
    case2=int(arr[p+1]+arr[p])
    if case1>case2:
        str+=arr[p]+arr[p+1]
    else:
        arr[p+1]+arr[p]
    arr=arr[2:]
    print(arr)