#dictionary정의
dict = {'email':"kiki@nnn",'age':5, 'sex':'male','weight':45}
print(dict.keys()) #dictionay 키들 출력
print(dict.values()) #value 출력
dict['tall'] = 164 #키와 value할당
print(dict)
del dict['sex'] #특정 키 삭제
print(dict)