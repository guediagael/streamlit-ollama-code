from pydantic import BaseModel
from typing import List, Any, Union


class Message(BaseModel):
    id: float
    role: str
    content: Any

class Chat(BaseModel):
    id:float
    title: Union[str, None]
    messages: List[Message]