from pydantic import BaseModel,Field
from typing import TypeVar, Optional

T = TypeVar("T")

class UserSchema(BaseModel):
    username:str = Field(
        ...
    )
    email:str
    password:str
    
    def __str__(self):
        return {
        "username": self.username,
        "email": self.email,
        "password": self.password
    }


def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "username": item["username"],
        "email": item["email"],
        "password": item["password"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
