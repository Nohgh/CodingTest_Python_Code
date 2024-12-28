#아이디어 힌트
import sys
input = sys.stdin.readline

# 1-2+3-4

# 일단 -를 기준으로 split을 한다 -> 1, 2+2, 4
# -기준으로 나온 것들에는 숫자로 구성되거나 +로 구성되어있다
#구성된 것들은 먼저 계산하고 -> 1,4,4
# 각각의 사이에 -를 취한다
# 1-4-4

express =input().rstrip()
arr=express.split('-')
for x in range(len(arr)):
    if arr[x].find('+')!=-1:
        newArr = []
        newArr=arr[x].split('+')
        for y in range(len(newArr)):
            newArr[y]=str(int(newArr[y]))
        arr[x]='+'.join(newArr)
        arr[x]=str(eval(arr[x]))
    else:
        arr[x]=str(int(arr[x])) #5+065와 같은 반례있음 
newStr = '-'.join(arr)
print(eval(newStr))

