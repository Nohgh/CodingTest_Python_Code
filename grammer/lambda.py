'''
람다: 익명함수를 생성할 떄 사용하는 키워드
간단한 연산이나 일회성 함수를 정의할 때 유용하게 사용

lambda 인자1,인자2, ... : 표현식
인자: 함수가 받을 입력값
표현식: 반환할 값을 지정, 한 줄로 작성, 결과가 반환됨

'''

# #숫자를 제곱하는 람다함수 
# s= lambda x: x**2
# print(s(2))

# #두 수를 더하는 람다함수
# add = lambda x,y: x+y
# print(add(2,4))

# #리스트의 정렬 기준으로 사용 -> 글자의 길이가 짧은 순으로 정렬 
# names = ["Alice", "Bob", "Charlie"]
# names.sort(key=lambda x : len(x))
# print(names)

#필터링
num=[1,2,3,4,5]
evens=list(filter(lambda x : x%2==0,num))
print(evens)
'''
filter(f,b)
f는 함수, True, False로 반환되어야 함
원본 데이터는 변하지 않고, 필터링된 요소만 반환한다.
반복 가능한 객체만 처리할 수 있다.
'''
# #맵핑
# s = list(map(lambda x : x**2,num))
# print(s)