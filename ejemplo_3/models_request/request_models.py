from pydantic import BaseModel

class calc_values(BaseModel):
    first_number: int
    second_number: int