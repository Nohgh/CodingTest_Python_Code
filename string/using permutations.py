#경우의 수 추출하는 방법
from itertools import permutations
dataset=['1','2','3','1']
printList =list(permutations(dataset,4))
arr=[]
for i in printList:
    sum=''
    for x in i:
        sum+=x
    arr.append(int(sum))
print(arr)
