from pydantic import BaseModel

class Client(BaseModel):
    name: str
    address: str
    phoneno: int
    