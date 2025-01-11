#이진탬색의 경우, 특정상황에서 많은 케이스를 비교해야하는 경우 이진탐색을 통해 해결할 수 있는 알고리즘이 보이는 경우가 대다수.
#따라서 많은 데이터를 순회하여, 특정 조건을 찾아야할 때 떠올리면 될 듯.
import sys
input=sys.stdin.readline
k,n=list(map(int,input().split()))
arr=[]
for _ in range(k):
	arr.append(int(input()))
arr.sort()
start=1
end=arr[len(arr)-1]
rst=0
while start<=end:
	total=0
	mid=(start+end)//2
	for i in arr:
		total+=i//mid
	if total<n: #11보다 작은 경우는 mid가 커서그럼.mid를 내리면 total값이 올라감
		end=mid-1
	else:#total이 크거나 같은 경우
		rst=mid
		start=mid+1
  
print(rst)
