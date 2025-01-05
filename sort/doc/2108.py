import sys
input = sys.stdin.readline

n=int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))
arr.sort()

print(round(sum(arr)/len(arr))) #산술평균
print(arr[len(arr)//2]) #중앙값

dic = dict() #빈도수를 위한 dic하나 생성, 2,3,4,2라는 값이 들어오면 2:1,3:1,4:1 이렇게 값이 저장된다.
for i in arr: #배열을 순회하며 
    if i in dic: #dic에 해당 값이 있다면 해당 dic의 값을 +1해준다.
        dic[i]+=1
    else:
        dic[i]=1 #아직 dic에 없는 값이라면 1로 초기세팅해준다.
        
mx = max(dic.values()) #빈도수 중 최대값 구하기 , dic의 value에는 빈도수가 저장됨, 
print("mx는 ",mx)
mx_dic=[]

for i in dic: #dic을 순회하며며
    if mx ==dic[i]: #최빈값의 key를 저장, 해당 i의 dic에서 value가 최대 빈도수라면 mx_dic에 추가해준다
        mx_dic.append(i)
        
if len(mx_dic)>1: #최빈값이 여러개인 경우
    print(mx_dic[1]) #두번째로 작은 값을 출력
else:
    print(mx_dic[0])
print(max(arr)-min(arr))
