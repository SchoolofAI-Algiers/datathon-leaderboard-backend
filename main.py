from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from creds import KAGGLE_USERNAME, KAGGLE_KEY
from config import COMPETITIONS

from typing import Union
from models import Response, ErrorResponse
from utils import get_competition_by_name
from service import fetch_public_leaderboard, fetch_local_leaderboard, get_datathon_leaderboard 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=['GET'],
)

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
    if competition == 'all':
        return Response(
            message='HAICK datathon leaderboard',
            data=get_datathon_leaderboard()
        )
    competition_obj = get_competition_by_name(competition)
    if competition_obj:
        if competition_obj['active'] == True:
            if competition_obj['type'] == 'online':
                return Response(
                    message=f'{competition} public leaderboard',
                    data=fetch_public_leaderboard(competition_name=competition)
                )
            elif competition_obj['type'] == 'local':
                return Response(
                    message=f'{competition} local leaderboard',
                    data=fetch_local_leaderboard(competition_name=competition)
                )
        else:
            return Response(
                message=f'{competition} is not active',
                data=[]
            )
    else:
        return ErrorResponse(
            message=f'{competition} is not involved in current datathon, please select from {COMPETITIONS}',
            error='Competition not found'
        )
