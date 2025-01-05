import sys
input=sys.stdin.readline
s=input().rstrip() 
dic=dict({'0':0,'1':0})

x=s[0] #1
dic[s[0]]=1
str=''
for i in s:
    if x!=i:
        x=i
        dic[i]+=1

print(min(dic.values()))
#깔끔스