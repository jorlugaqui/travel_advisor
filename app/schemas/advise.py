from typing import Union
from pydantic import BaseModel


class Advise(BaseModel):
    query: str
    instructions: Union[list[str], None] = None
