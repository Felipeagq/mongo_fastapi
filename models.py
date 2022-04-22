from lib2to3.pytree import Base
from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")

class RequestBook(BaseModel):
    id: str = None
    title: str
    description: str 


class ResponseBook(BaseModel):
    code: str
    status: str
    message: str
    Result: Optional[T] = None