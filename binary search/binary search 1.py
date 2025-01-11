#재귀를 사용한 이진탐색
def bs(array,target,start,end):
    if start>end: #정렬을 마친경우
        return None 
    mid=(start+end)//2 # 중간값은 끝과 시작점을 더해 나누고, 소수점은 없앤다.
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return bs(array,target,start,mid-1)    
    else:
        return bs(array,target,mid+1,end)
    
n,target=list(map(int,input().split()))
array=list(map(int,input().split()))

result=bs(array,target,0,n-1)
if result ==None:
    print("원소가 존재하지 않습니다")
else:
	print(result+1)
    
