import sys
input = sys.stdin.readline

# 55-50+40-10

str =input().rstrip()
newStr="" 

while str!="":
    minusIdx = str.find('-')
    
    if minusIdx !=-1:
        newStr=str[:minusIdx+1] # -까지 newStr에 할당
        str=str[minusIdx+1:] #처음 - 를 newStr로 보내고 다음 -가 있는지 판별 
        
        if str.find('-')==-1 and str.find('+')==-1: #+, -가 없는 숫자만 오는 경우 
            newStr+=str[0:] #여기까지 왔으면 -이후에 숫자만 오고 식이 끝남 -> 바로 출력가능
            print(eval(newStr))
            str="" 
            break
        
        #+ or - 존재 
        newStr+='(' # x - ( 상태 
        if str.find('-')!=-1: #다시 -가 오는 경우 
            newStr+=str[0:str.find('-')]+")"+str[str.find('-')] # - 앞까지 )로 묶음, - 붙임
            str=str[str.find('-')+1:] #-까지 newStr로 보내고 -이후의 문자로 업데이트  
        else:
            newStr+=str+")"
            print(eval(newStr)) 
            str=""
            break
            
                        
    else:
        newStr+=str
        print(eval(newStr)) 
        str=""
        break
        