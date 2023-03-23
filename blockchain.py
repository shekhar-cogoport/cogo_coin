from hashlib import sha256
from comm_database.comm_database_client import temp

def updatehash(*args):
   hashing_text=""; h=sha256()
   for arg in args:
      hashing_text+=str(arg)

   hashing_text=hashing_text.encode('utf-8') 
   
   h.update(hashing_text) 
   
   return h.hexdigest()

class Block():
   data=None
   hash=None
   nonce=0
   previous_hash = "0" * 64
   def __init__(self,data,number=0): 
     self.data=data
     self.number=number

   def hash(self):
     return updatehash(self.previous_hash,self.number,self.data,self.nonce)  

   def __str__(self):
     return str("Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n" %(
       self.number,
       self.hash(),
       self.previous_hash,
       self.data,
       self.nonce
     ))
   

class BlockChain():
  difficulty=4 

  def __init__(self,chain=[]):
    self.chain=chain

  def add(self,block):
    self.chain.append({'hash': block.hash(),
                       'previous': block.previous_hash,
                       'number': block.number,
                       'data': block.data,
                       'nonce': block.nonce
                     })  

  def mine(self,block):
    try:
      block.previous_hash=self.chain[-1].get('hash')
    except IndexError:
      pass

    while True:
      if block.hash()[:self.difficulty] == "0" * self.difficulty:
          self.add(block); break
      else:
         block.nonce+=1    

  def isValid(self):
     for i in range(1,len(self.chain)):   
       _previous = self.chain[i].get('previous_hash')
       print('hash',self.chain[i-1])
       _current = self.chain[i-1].hash()
       if _previous != _current or _current[:self.difficulty] != "0"*self.difficulty:
         return False
     return True      

def main():
  conn=temp()
  cur = conn.cursor()
             
  query ="SELECT * FROM cogoone_timelines WHERE  status='active'" 
               
  cur.execute(query)

  results = cur.fetchall()
  for result in results:
    print(result)

  blockchain=BlockChain()
  database=["hello world","whats's up","hello","bye"]

  num=0
  for data in database:
    num=num+1
    blockchain.mine(Block(data,num))

  for block in blockchain.chain:
    print(block)

  print(blockchain.isValid())  


if __name__ == '__main__':
  main() 


