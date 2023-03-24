from app import session
from comm_database.comm_database_client import temp

class Table():
    def __init__(self,table_name,*args):
        self.table=table_name
        self.column="(%s)"%",".join(args)

        if isnewTABLE(table_name):
          cur=temp['cur']
          cur.execute("Create table %s%s" %(self.table,self.column))
          cur.close()

    def getall(self):
       query="Select * from %s" %self.table
       result=temp['cur'].execute(query)
       data = temp['cur'].fetchall()
       return data      
    
    def getone(self,search,value):
       data={}
       query="Select * from %s where %s = \"%s\"" %(self.table,search,value)
       results=temp['cur'].execute(query)
       if results > 0: 
        data=temp['cur'].fetchone()
       temp['cur'].close()
       return data 
    
    def deleteone(self,search,value):
       query="Delete from %s where %s =\"%s\""%(self.table,search,value)
       results=temp['cur'].execute(query)
       temp['conn'].commit

    def insert(self,*args):
       data=""

       for arg in args:
          data+="\"%s\","%(arg)

       query="Insert into %s%s Values(%s)"%(self.table,self.column,data[:len(data)-1])
       temp['cur'].execute(query)
       temp['conn'].commit()
       temp['cur'].close()

def isnewTABLE(tableName):
    try:
      result=temp['cur'].execute("select * from %s" %tableName)
      temp['cur'].close()
    except:
      return True
    else:
      return False
    
 

    
   
