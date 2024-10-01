'''
Linear Probing기법
방식에서 공간을 늘린 방법 ( 공간 확장 )
'''

class HashTable:
    def __init__(self,n):
        self.n = n 
        self.hash_table = list([0 for i in range(n)])
        
    def hash_function(self, key):
        return key % self.n
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
        
ht= HashTable(11)
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
