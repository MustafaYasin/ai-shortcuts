from pydantic import BaseModel
from typing import Optional

class Framework(BaseModel):
    id: int
    title: str
    description: str

class FrameworkUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
