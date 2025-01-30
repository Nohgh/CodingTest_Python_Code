dic={'name':"Noh","phone":'010888888',"birth":"11"}
#키와 value로 이루어짐 value에 다양한 데이터 구조(list, string 등)을 넣을 수 있습니다
print(dic)
a={1:'a'}
a[2]='aa'
a[3]=[1,2,3]
del a[2]
print(a)
print(a.keys())
print(a.items())
print(a.get(1))