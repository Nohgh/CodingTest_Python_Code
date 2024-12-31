def d(n):
    my_sum=n
    sn = str(n)
# 숫자를 문자형으로 다루어 하나씩 순회하여 매개변수로 들어온 d(n)을 계산한다.
# 내가 푼 코드의 실행시간 보다 현저히 낮은 실행시간을 기록함, 숫자를 다룰 때 str로 해결 할 수 있는지에 대한 접근 방법도 생각하면 도움 될 듯

    for s in sn: 
        my_sum +=int(s)
    return my_sum

MAX = 10_000 + 1
my_arr=[True]*MAX

for i in range(1,MAX):
    rst = d(i)

    if rst < MAX :
        my_arr[rst]=False

for i in range(1, MAX):
    if my_arr[i]: 
        print(i)