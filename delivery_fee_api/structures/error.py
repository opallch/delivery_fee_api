from pydantic import BaseModel

class ErrorResponse(BaseModel):
    code: int
    name: str
    description: str 
    status: str = 'error'
