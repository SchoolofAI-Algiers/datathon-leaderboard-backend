from fastapi import FastAPI

from creds import KAGGLE_USERNAME, KAGGLE_KEY
from config import COMPETITIONS

from typing import Union
from models import Response, ErrorResponse
from service import fetch_public_leaderboard

app = FastAPI()

@app.get('/')
async def root():
    return {
        'message': 'HAICK is a datathon organized by School Of AI Algiers - 2024'
    }

@app.get("/{competition}/leaderboard/public")
async def get_public_leaderboard(competition: str) -> Union[Response, ErrorResponse]:
    '''
    Get a Kaggle competition's public leaderboard
    '''
    if competition in COMPETITIONS:
        return Response(
            message=f'{competition} public leaderboard',
            data=fetch_public_leaderboard(competition_name=competition)
        )
    else:
        return ErrorResponse(
            message=f'{competition} is not involved in current datathon, please select from {COMPETITIONS}',
            error='Competition not found'
        )
