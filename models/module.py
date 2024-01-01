from pydantic import BaseModel

class Module(BaseModel):
    framework_id: int
    id: int
    title: str
    description: str
