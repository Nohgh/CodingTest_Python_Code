
# 1.짝수 필터링

# 주어진 리스트 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 짝수만 골라 리스트로 만드세요.
arr1 = [i for i in range(1,10) if i %2 ==0]
print(arr1)

# 2.제곱 값 계산

# 주어진 리스트 [1, 2, 3, 4, 5]의 각 값을 제곱한 리스트를 만드세요.

arr2 = [1,2,3,4,5]
arr2 = [i**2 for i in arr2 ]
print(arr2)


# 3.대문자로 변환

# 주어진 문자열 리스트 ['apple', 'banana', 'cherry']의 각 단어를 대문자로 변환하세요.

arr3 = ['apple', 'banana', 'cherry']
arr3  = [i.upper() for i in arr3]
print(arr3)


# 4.짝수는 제곱, 홀수는 그대로

# 주어진 리스트 [1, 2, 3, 4, 5]에서 짝수는 제곱하고, 홀수는 그대로 두세요.
arr4 = [1,2,3,4,5]
arr4 = [i**2 if i %2==0 else i for i in arr4]
# [참일 때 값 if 조건 else 거짓말일때 값 for 항목 in 리스트]
# if와 else 의 각 값의 위치가 중요
print(arr4)

# 5.2차원 리스트 펼치기

# 2차원 리스트 [[1, 2], [3, 4], [5, 6]]를 1차원 리스트로 변환하세요.
arr5=[[1, 2], [3, 4], [5, 6]]
arr5=[x for i in arr5 for x in i] #중첩으로 for문을 사용함
print(arr5)


# 6.문자열 길이 필터링

# 주어진 문자열 리스트 ['hi', 'hell', 'world', 'python']에서 길이가 4 이상인 문자열만 골라내세요.
arr6 = ['hi', 'hello', 'world', 'python']
arr6 = [ i for i in arr6 if len(i)>4]
print(arr6)

#2차원 배열 0으로 초기화 4x3배열
arr7 = [[0]*3 for _ in range(4)]
print(arr7)