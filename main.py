from fastapi import FastAPI

from creds import KAGGLE_USERNAME, KAGGLE_KEY
from config import COMPETITIONS

from models import Team
from service import get_public_leaderboard, get_private_leaderboard

app = FastAPI()

@app.get('/')
async def root():
    return {
        'message': 'School Of AI Algiers'
    }

@app.get("/{competition}/leaderboard/public")
async def get_public_leaderboard(competition: str) -> list[Team]:
    '''
    Get a Kaggle competition's public leaderboard
    '''
    if competition in COMPETITIONS:
        return {
            'message': f'{competition} public leaderboard',
            'data': get_public_leaderboard(competition_name=competition)
        }
    else:
        return {
            'message': f'{competition} is not involved in current datathon',
        }