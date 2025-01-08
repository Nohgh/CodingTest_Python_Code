from itertools import permutations
import sys
input=sys.stdin.readline

s=input().rstrip()
if s.count('0')==0:
    print(-1)
else:
	printList =list(permutations(s,len(s)))
	arr=[]
	for i in printList:
		sum=''
		for x in i:
			sum+=x
		if sum[0]!='0' and int(sum)%30 ==0:
			arr.append(int(sum))
	arr.sort(reverse=True)
	print(arr[0])
