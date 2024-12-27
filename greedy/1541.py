import sys
input = sys.stdin.readline
'''
55-50+40-10
10
'''

'''
55-(50+40-(10)...)
'''
express =input().rstrip() #4-1
expressArr="" 
while express!="":
    minusIdx=express.find('-') #1
    if minusIdx != -1: #-가 있다면 
        expressArr=expressArr+express[:minusIdx+1]+'(' # -와 그 앞의 식 + ( 을 배열에 담음
        express=express[minusIdx+1:] # - 이후의 식으로 식을 업데이트
    else:
        if expressArr !="":
            expressArr+=express +")"
            print(eval(expressArr))
        else:
            print(eval(express))
        express=""
        break
