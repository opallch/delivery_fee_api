from pydantic import BaseModel

class HTTPErrorResponse(BaseModel):
    """Response payload in case of HTTP Errors."""
    code: int
    name: str
    description: str 
    status: str = 'error'
