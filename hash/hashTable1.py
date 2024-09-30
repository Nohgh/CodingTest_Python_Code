class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])
    
    def hash_function(self, key):
        return key % 8
    
    def insert(self, key, value):
        hash_value = self.hash_function(hash(key))
        print("hash(key) 결과 = ",hash(key))
        self.hash_table[hash_value]=value
    
    def read(self, key):
        hasH_value=self.hash_function(hash(key))
        return self.hash_table[hasH_value]
    
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

# hash(key) 결과 =  1
# [0, 'a', 0, 0, 0, 0, 0, 0]
# hash(key) 결과 =  2594680629639167691
# [0, 'a', 0, 'kang', 0, 0, 0, 0]
# hash(key) 결과 =  2
# [0, 'a', 'b', 'kang', 0, 0, 0, 0]
# hash(key) 결과 =  3
# [0, 'a', 'b', 'c', 0, 0, 0, 0]
# ht.read(2) 결과 =  b
# hash(key) 결과 =  4
# [0, 'a', 'b', 'c', 'd', 0, 0, 0]

#TODO: 위의 결과처럼 해당 해쉬 테이블에는 문제점이 있음 
'''
'name','Noh' 쌍이 삭제를 안함에도 (2,'b')가 들어가자 없어진것. 
이는 hash의 계산이 겹쳐서 발생한 충돌 Collision이라 한다.

'''