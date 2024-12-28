import sys

input = sys.stdin.readline

n = int(input().strip())

table = []

for i in range(n):
    s, e = map(int, input().split())
    table.append((s, e))

table.sort(key=lambda x: x[0])
table.sort(key=lambda x: x[1])
print(table)

end = -1
ans = 0

for i in range(n): #포인터 처럼 동작, end를 초기는 -1, 이후에는 table에 있는 값의 1번 인덱스 값으로 설정, 
    #순회하는 table의[0]번쨰와 비교하여 비교하는 값이 크거나 같은 경우에만, end를 업데이트, 회의의 개수를 증가
    if table[i][0] >= end:
        end = table[i][1]
        ans += 1

print(ans)
#핵심은 배열을 포인터처럼 활용하여, 이전 배열과의 비교를 쉽게 한다.