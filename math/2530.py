H, M, S = map(int, input().split()) #14 30 0
T = int(input())  # 더하는 시간  200

# H M S T 
S += T % 60 # 초 더하는 시간에서 60나머지 //s=20
T = T // 60 # 시간은  //3
if S >= 60:
    S -= 60
    M += 1 #여기서 분 계산 (60초 이상시 1)
M += T % 60  # 30+ 3 % 60 => m= 33
T = T // 60  #3//60 => 0 시간은 0 
if M >= 60:
    M -= 60
    H += 1
H += T % 24 #h=14
if H >= 24:
    H -= 24
print(H,M,S)