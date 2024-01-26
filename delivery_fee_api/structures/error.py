from pydantic import BaseModel

class ErrorResponse(BaseModel):
    code: str
    name: str
    description: str 
    status: str = 'error'
