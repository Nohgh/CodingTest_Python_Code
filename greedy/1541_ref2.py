import sys 
#1-2-3+4
s = sys.stdin.readline().strip().split('-') #-를 기준으로 분리 , -가 없다면 하나의 배열에 할당 
#s=1,2,3+4
temp =[] #임시 배열 생성
for i in s:#배열 순회 1,2,3+4
    cnt = 0 #해당 s의 합 
    for j in i.split('+'): #배열 내부의 +로 나누고 순회
        #해당 for문에서 i문자열에 +가 없다면 i그 자체에 대한 값으로 됨
        cnt += int(j) #+로 나눈 값들의 합으로 cnt를 업데이트
        #3+4인 경우에 
        #cnt+= 3, cnt+=4 
    temp.append(cnt) #각 s를 순회하며 나온 합을 temp에 저장 
result = temp[0] #result = 임시배열의 첫 값 
for i in temp[1:]: #첫 값 이후의 값들을 순회 
    result -= i #합 배열의 첫 값에 이후의 값들에 대해 계속 마이너스
    #1= 1 - 2
    #-1=-1-7
    #-8
print(result)

# 핵심은 -을 기준으로 나누면 그 각각의 값에는 +가 포함된 식이나 숫자만 남게됨
#각 식에 대해 합을 구하고 각 식에 대한 합을 저장할 배열 하나를 할당
#각 식의 합을 저장한 배열에 대해 첫 값은 따로 뺴고
#그 다음 값들 부터 첫값에서 계속 - 하면 
#-를 기준으로 값들을 묶어 합을 구하고 -를 한것과 동일