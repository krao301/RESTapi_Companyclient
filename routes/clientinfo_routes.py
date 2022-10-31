from fastapi import APIRouter

from models.clientinfo_model import Client
from config.database import collection_name

from schemas.clientinfo_schema import clients_serializer, client_serializer
from bson import ObjectId

client_api_router = APIRouter()

# retrieve
@client_api_router.get("/")
async def get_clients():
    clients = clients_serializer(collection_name.find())
    return {"status": "ok" ,"data": clients}

@client_api_router.get("/{id}")
async def get_client(id: str):
    client = clients_serializer(collection_name.find_one({"_id": ObjectId(id)}))
    return {"status": "ok", "data" : client}

# post
@client_api_router.post("/")
async def create_client(client: Client):
    _id = collection_name.insert_one(dict(client))
    client= clients_serializer(collection_name.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data" : client}

# update
@client_api_router.put("/{id}")
async def update_client(id: str, client: Client):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(client)
    })
    client= clients_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status":"ok" , "data": client}

# delete
@client_api_router.delete("/{id}")
async def delete_client(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok","data" : []}