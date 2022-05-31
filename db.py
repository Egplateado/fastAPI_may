from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    Age: int
    SSN : Optional[str] 

### random generate a DB
import random
names = ['JOEL','MAEVE','RUBY','MILLY','ERICK','JACOKC','OLA']
db = []
for x in range(200):
    name = random.choice(names)
    suName = random.choice(names)

    SSN = ''.join([str(random.randint(1,9)) for _ in range(9)])

    dumyUser = {'id':x,'name':name+' '+suName,'email':name+'@mail.com','Age':random.randrange(18,80),'SSN':SSN}

    d = User(id=dumyUser['id'],name=dumyUser['name'],email=dumyUser['email'],Age=dumyUser['Age'],SSN=dumyUser['SSN'])
    
    db.append(d)
#print(db)


###
### API definitions
###

@app.get('/') # get all db
def root(): 
    return db 

@app.get('/older_than{num}') # get data > num
def getOrders(num: int ):
    users = [u for u in db if u.Age > num]
    return users

############

@app.post("/items/") # submit data
def create_item(item: User):
    db.append(item)
    return item

###########


@app.put('/insert{data_id}')
def insertUser(data_id:int, data:User): # put needs id and data
    print(data)
    db.append(data)
    return {'ANS':'userInserted'}

#############

@app.patch("/items/{item_id}", response_model=User)
async def update_item(item_id: int, item: User):
    stored_item_model = db[item_id] # item from DB
    update_data = item.dict() # item from HTTP 
    updated_item = stored_item_model.copy(update=update_data) # update
    db[item_id] = updated_item # replace
    return updated_item

#########

@app.delete('/delete{user_id}')
def deleteUser(user_id:int):
    global db
    lenInit = len(db)
    db = [u for u in db if u.id!=user_id]
    print(lenInit , len(db))
    if lenInit != len(db):
        return {'ANS':'user Deleted'}
    else:
        raise HTTPException(status_code=404, detail="User not found")
        return {'ANS':'user not found'}