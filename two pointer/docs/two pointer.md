# 투 포인터

배열 내부에 자연수로 구성된 숫자들이 있고,

그 숫자들의 합이 x인 경우의 수를 카운트하여 출력하고자 할 때

일반적으로 떠올릴 수 있는 방법은 for문을 사용한 o(n^2)의 코드.

이를 선형적으로 0(n)으로 풀 수 있는 방법이 바로 투 포인터인데

### 투 포인터 코드 말로 설명

코테 책에서 자세한 원리 참고하기!

```python
n=5
m=5
data=[1,2,3,2,5]
count=0
interval_sum=0
end=0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum+=data[end]
        end+=1
    if interval_sum == m:
        count+=1
    interval_sum-=data[start]
print(count)
```

### 코드가 마음에 안든다.

위의 코드가 투 포인터의 대표적인 예제인데

책에서 저자가 설명한 그림과 코드에서 동작의 매칭이 너무 잘되지 않았고,

어거지로 이해한 후 1940문제를 만났다.

위의 코드로 재시된 입력에 대한 답을 얻었지만 여러 반례에 막혀, 방법을 찾던 중
어떤 포스트에서 start와 end를 끝과끝에 배치하고 두 포인터의 합만을 비교하며
위치를 조정하는ㄴ것을 봤다.

해당 방식이 예전부터 내가 자주 사용하던 방식이고 직관적으로 이해하기 편하기 때문에 포스트에 있던 코드를 바탕으로 투 포인터 문제를 풀었고, 결과는 통과를 받았다.

## 포스트에서 제시된 코드

```python
#투 포인터의 대표 문제
import sys
input=sys.stdin.readline

n=int(input()) #재료의 개수
m=int(input())#갑옷을 만드는데 필요한 수, 목표

l=list(map(int,input().split()))#n개의 재료들이 가진 고유한 번호
l.sort()

start,end=0,len(l)-1
cnt=0
while start<end:
    result=l[start]+l[end]
    if result>m:
        end-=1
    elif result<m:
        start+=1
    else:
        cnt +=1
        start+=1
        end -=1
print(cnt)
```

위와 같이 직관적인 방법으로 투 포인터를 해결하는것이 좋다는 생각이 들었다.

https://velog.io/@mquat/python-%EA%B8%B0%EC%B4%88-%EB%B0%B1%EC%A4%80-1940%EB%B2%88-%ED%88%AC%ED%8F%AC%EC%9D%B8%ED%84%B0
