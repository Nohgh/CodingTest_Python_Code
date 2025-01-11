n,m=list(map(int,input().split())) #4 6
array=list(map(int,input().split()))# 19 15 10 17

start=0
end=max(array)

result=0

while(start <= end):
    total=0
    mid=(start+end)//2
    for x in array:
        if x >mid:#떡은 제단기 mid의 길이보다 큰 경우에만 짤림
            total+= x-mid
    if total < m: #짤린 길이들이 원하는 m보다 적은 경우= 더 잘라야함= 중간이전의 값들로 제단기를 설정
        end=mid-1
    else: #짤린 total이 m과 같거나 큰 경우
        result=mid #최대한 덜 잘랐을떄가 정답
        start=mid + 1
print(result)