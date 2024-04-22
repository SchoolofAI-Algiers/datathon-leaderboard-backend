import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

from creds import KAGGLE_USERNAME, KAGGLE_KEY
from utils import preprocess_leaderboard

api = kaggle.KaggleApi()
api.authenticate()

def get_public_leaderboard(competition_name):
    public_leaderboard = api.competition_view_leaderboard(competition_name)
    return preprocess_leaderboard(public_leaderboard)

def get_private_leaderboard():
    pass