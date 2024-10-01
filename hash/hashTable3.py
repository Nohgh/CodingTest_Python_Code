
'''
Linear Probing기법
close Hashing기법 중 하나로 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 방법이다/
충돌이 일어나면 해당 hash value(address)의 다음 index부터 맨 처음 나오는 빈공간에 저장하는 기법이다.
=> 저장공간 활용도의 증가 
'''
class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])
        
    def hash_function(self, key):
        return key % 8
    def insert(self, key, value):
        gen_key= hash(key)
        hash_value = self.hash_function(gen_key)
        
        if self.hash_table[hash_value] != 0:
            for i in range(hash_value,len(self.hash_table)):
                if self.hash_table[i]==0:
                    self.hash_table[i]= [gen_key,value]
                    return
                elif self.hash_table[i][0]==gen_key:
                    self.hash_table[i][1]=value
                    return
        else:
            self.hash_table[hash_value]=[gen_key,value]
        
    def read(self,key):
        gen_key= hash(key)
        hash_value = self.hash_function(gen_key)
        
        if self.hash_table[hash_value] != 0:
            for i in range(hash_value, len(self.hash_table)):
                if self.hash_table[i]==0:
                    return None
                elif self.hash_table[i][0]==gen_key:
                    return self.hash_table[i][1]
        else:
            return None
        
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
'''
해당 알고리즘의 단점 
미리 지정한 자릿 수를 넘어가면 충돌이 일어난다.
=> 공간을 확장하는 방법을 사용한다.
'''