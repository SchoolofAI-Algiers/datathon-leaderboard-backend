from pydantic import BaseModel

class Team(BaseModel):
    name: str
    score: float