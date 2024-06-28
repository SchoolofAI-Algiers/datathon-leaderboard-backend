from typing import List
from pydantic import BaseModel

class Team(BaseModel):
    name: str
    score: float
    
class Leaderboard(BaseModel):
    competition: str
    teams: List[Team]
    
class Response(BaseModel):
    message: str
    data: list[Team]
    
class ErrorResponse(BaseModel):
    message: str
    error: str