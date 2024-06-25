from pydantic import BaseModel

class Team(BaseModel):
    name: str
    score: float
    
class Response(BaseModel):
    message: str
    data: list[Team]
    
class ErrorResponse(BaseModel):
    message: str
    error: str