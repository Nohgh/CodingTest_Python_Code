def frequency(s):
    dic = {
        '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
        '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p',
        '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w',
        '24#': 'x', '25#': 'y', '26#': 'z'
    }
    alp = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    i = 0
    rst = []

    while i < len(s):
        # 괄호 처리
        if s[i] == '(':
            num = int(s[i + 1])  # 괄호 안의 숫자 추출
            letter = rst[-1]  # 이전에 나온 문자
            for _ in range(num):  # 숫자만큼 그 문자를 반복해서 추가
                rst.append(letter)
            i += 3  # 괄호 처리 후 3칸 이동 (괄호 열고 숫자, 괄호 닫힘)
            continue  # while문을 계속 돌리기 위해 continue 사용
        
        # 10#~26# 처리
        if i + 2 < len(s) and s[i + 2] == '#':
            rst.append(dic[s[i] + s[i + 1] + s[i + 2]])
            i += 3  # 3칸 이동
        else:
            rst.append(dic[s[i]])
            i += 1  # 1칸 이동
    
    # 알파벳 빈도 계산
    strr = []
    for x in alp:
        cnt = rst.count(x)
        strr.append(cnt)

    return strr

if __name__ == '__main__':
    s = input().strip()  # 입력 받기
    result = frequency(s)  # 함수 호출
    for x in result:
        print(x)
