from dataclasses import dataclass
from typing import List
from pydantic import BaseModel

@dataclass
class Type:
    name: str

@dataclass
class TypeSlot:
    slot: int
    type: Type

@dataclass
class Pokemon(BaseModel):
    id: int
    name: str
    types: List[TypeSlot]

    class Config:
        extra = 'ignore'
