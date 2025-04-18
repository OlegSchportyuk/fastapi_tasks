from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskID(BaseModel):
    ok: bool = True
    task_id: int
