import sys
input = sys.stdin.readline

n = int(input())

lst = input().split() #바로 배열로 들어감
q = max(map(lambda x : len(x),lst)) #map을 통해 lst배열의 각 요소에 람다함수를 적용, 람다에서는 lst각 요소의 길이를 반환
#따라서 q에는 lst에 들어온 값들 중 가장 큰 자리수의 길이가 저장됨

lst.sort(key= lambda x : int(x.ljust(q,'0')) ,reverse=True    )

'''
ljust: 문자열 메서드, 문자열을 왼쪽으로 정렬, 오른쪽에 지정한 문자를 추가하여 원하는 길이만큼 확장하는 역할을 한다.
해당 코드에서는 q만큼 문자열의 총 길이를 지정하고, 빈자리를 0으로 채운다.
int( )내부에 x.ljust가 들어갈것이기 때문에 람다의 x에 대해 왼쪽 정렬한 문자를 정수형으로 바꾼다.
내림차순 정렬하여, 입력받은 숫자 중 가장 큰 자리의 숫자로 모두 맞추고(오른쪽에 0을 추가) 가장 큰 숫자로 정렬함
'''


ans = "" #가장 큰 수 
for x in lst: # 9 12 5 51 52-> 90 12 
    ans = max(x+ans,ans+x) # 912, 129에서 max를 ans로 업데이트   -> 912
    #912 = (5912, 9125)비교 ...
if int(ans) == 0: #가장 큰 수가 담길 ans의 값이 0인지 확인 
    print(0)
else:
    print(ans)  
    
#idea: 수들을 비교하기 위해 자리수를 가장 큰 자리수로 설정하고 
#앞 뒤로 값들을 붙여 대소관계를 파악하여 가장 큰 수를 만든다.
#람다와 ljust함수를 통해 정렬을 잘 하는것이 관건