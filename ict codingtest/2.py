import sys
import math

def maxSubsetSum(k):
    rst = []
    for x in k:
        sum = 0
        # x의 약수를 1부터 sqrt(x)까지 탐색
        for i in range(1, int(math.sqrt(x)) + 1):
            if x % i == 0:
                sum += i
                if i != x // i:  # x // i가 i와 다르면 두 번째 약수도 더해줌
                    sum += x // i
        rst.append(sum)
    return rst

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    rst = maxSubsetSum(arr)
    print('\n'.join(map(str, rst)))
