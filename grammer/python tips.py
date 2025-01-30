#문자열 뒤집기
string="abcdefg"
print(string[::-1]) 

#중복제거하기 
a=[1,1,1,1,2,2,2,2,33,3,4,55,55]
print(list(set(a)))

#키와 value 한번에 리턴하기
arr=['a','b','c']
for idx,value in enumerate(arr):
    print(idx,value)

print("-----")
#길이가 같은 두 개 이상의 iterable객체를 동시에 for문 돌리기
temp1=[1,3,5]
temp2=[2,3,4]

for n1,n2 in zip(temp1,temp2):
    print(n1,n2)

import bisect
lst=[1,3,5,6,6,8]
print(bisect.bisect_left(lst,4))
print(bisect.bisect_left(lst,6))
print(bisect.bisect_right,6)
