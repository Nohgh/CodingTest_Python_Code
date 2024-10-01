#TODO: hashTable1에서 발생한 충돌 해결 알고리즘

# Chaining 기법
'''
Open Hashing 기법 중 하나
해쉬 테이블 저장공간 외에 공간을 더 추가해서 사용하는 방법
충돌이 발생시 , 링크드 리스트로 데이터를 추가로 뒤에 연결시키는 방법이다.
'''
class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])
    
    def hash_function(self, key):
        return key % 8
    
    def insert(self, key, value):
        gen_key=hash(key) #키를 hash 돌려 gen_key를 생성한다
        hash_value= self.hash_function(gen_key) # hash_func에 넣어 해시를 생성
        
        if self.hash_table[hash_value] != 0 : #해시테이블에 넣는 해시 idx가 이미 있는 경우
            for i in range(len(self.hash_table[hash_value])): #해시 내부의 값 길이 만큼 반복
                if self.hash_table[hash_value][i][0]==gen_key: #생성한 키가 이미 존재하는 경우
                    self.hash_table[hash_value][i][1]=value #0은 키, 1은 value로 인덱스 교체한다.
                    return
            self.hash_table[hash_value].append([gen_key,value]) #해당 hash_Value를 사용하지 않는다면 키와 값을 넣어준다.
        else:
            #해당 hash_value를 사용하고 있지 않는 경우 
            self.hash_table[hash_value]=[[gen_key,value]]
    #FIXME: read작성 https://davinci-ai.tistory.com/19
    def read(self, key):
        gen_key=hash(key)
        hash_value = self.hash_function(gen_key)
        
        if self.hash_table[hash_value]!=0:
            for i in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][i][0] == gen_key:
                    return self.hash_table[hash_value][i][1]
            return None #동일한 키가 존재하지 않을때 return None
        else: return None
    def print(self):
        print(self.hash_table)
        
ht= HashTable()
ht.insert(1,'a')
ht.print()

ht.insert('name','kang')
ht.print()

ht.insert(2,'b')
ht.print()

ht.insert(3,'c')
ht.print()
print('ht.read(2) 결과 = ',ht.read(2))

ht.insert(4,'d')
ht.print()
