import itertools

def findSimilar(a, b):
    # a와 b의 길이가 다르면 유사하지 않음
    if len(a) != len(b):
        return 0
    
    # a와 b에서 1의 위치 찾기
    sol = a
    for x in a:
        if a.count(x) != b.count(x):
            sol = b
            break

    # 순열을 구하고, 각 순열을 문자열로 변환
    perm = set(itertools.permutations(sol))

    # 앞자리가 0인 순열을 제외
    result = [''.join(p) for p in perm if p[0] != '0']

    
    return len(result)

if __name__ == '__main__':
    a = input().strip()
    b = input().strip()
    
    rst = findSimilar(a, b)
    print(rst)
