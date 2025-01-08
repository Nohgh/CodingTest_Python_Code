import sys
input=sys.stdin.readline
#해법: 30의 배수는 3의 배수이다.
#3의 배수가 가지는 특징은 각 자릿수의 숫자를 모두 더하면 3의 배수가 나온다는 점이다.
#3,6,9,12,15,18,21 모두 각 자리의 숫자를 더하면 3의 배수가 나옴
#따라서 s를 입력받고, 0이 없으면 -1을 출력하고, 그렇지 않다면  sum을 업데이트해가면서 3의 배수인지 계속 확인한다.
s=list(input().rstrip())
s=sorted(s,reverse=True)
if s[-1]!='0':
    print(-1)
else:
	sum=0
	for i in s:
		sum+=int(i)
	if sum %3 !=0:
		print(-1)
	else:
		print(''.join(s))