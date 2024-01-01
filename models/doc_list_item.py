from pydantic import BaseModel

class DocListItem(BaseModel):
    module_id: int
    title: str
    description: str
    code: str
