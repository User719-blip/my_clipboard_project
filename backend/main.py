from fastapi import FastAPI , HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pydantic import BaseModel 
import os
from dotenv import load_dotenv

#to load the enviroment var
load_dotenv()

#MONGO db setup
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# FAST API SET UP
app = FastAPI()

# CoRoS SETUP
app.add_middleware
(
CORSMiddleware,
allow_origins:=["*"],
allow_credentials:=True,
allow_methords:=["*"],
allow_headers:=["*"],
)

#pydentric model
class clipboarditem(BaseModel):
    content : str

#routers
@app.post("/add")
async def add_clipboard_item(item : clipboarditem):
    result = collection.insert_one(item.dict())
    return {"id" : str(result.inserted_id)}

@app.get("/get_all")
async def get_all_clipboard_items():
    item = list(collection.find({}, {"_id": 0}))
    return item

@app.delete("/delete_all")
async def delete_all_clipboard_items():
    collection.delete_many({})
    return {"massage": "all items deleted sucees fully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app , host = "0.0.0.0",port=8000)