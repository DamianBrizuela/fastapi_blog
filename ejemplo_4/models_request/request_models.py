from pydantic import BaseModel

class data(BaseModel):
    str_data: str
    some_number: int