arr=[[3,1],[4,5],[1,2],[4,4],[2,3]]
#2번째 요소로 정렬하고 2번째 요소가 같다면 첫번째 요소로 정렬하라
arr=sorted(arr, key=lambda x:(x[1],x[0]))
print(arr)

array = [[50, "apple"], [30, "banana"] , [400, "melon"]]
#int를 기준으로 정렬하기
array.sort(key=lambda x:x[0])
print(array)


array = [("A", 18, 300000) , ("F", 24, 10000), ("T", 24, 200000),("Q",24,5000000), ("B", 70, 5000)]
#2번쨰로 정렬하고, 같다면 3번째요소가 큰순으로 정렬
array.sort(key=lambda x:(x[1],-x[2]))
print(array)

#f'...'는 문자열 안에 변수를 삽입하거나 표현식을 계산한 결과를 바로 넣을 수 있도록 하는 문자열 포매팅 방식이다.
#{}안에 변수를 넣으면 해당 변수의 값이 문자열에 삽입된다.
a=1
b=2
c=3

def w(a,b,c):
    print(a,b,c)
    
print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
