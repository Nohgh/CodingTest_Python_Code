import sys
input = sys.stdin.readline

express =input().rstrip()

while(express!=""):
    if express.find('-'):
        minusIdx=express.index('-')
    else:
        print(eval(express))
        break
print("식에 아무것도 없네요")