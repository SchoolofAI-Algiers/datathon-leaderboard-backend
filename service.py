import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

import json
import numpy as np
from typing import List
from utils import preprocess_leaderboard, preproces_datathon_leaderboard, get_competition_coef
from models import Leaderboard
from config import COMPETITIONS

# configure_credentials()
api = kaggle.KaggleApi()
api.authenticate()

def fetch_public_leaderboard(competition_name):
    public_leaderboard = api.competition_view_leaderboard(competition_name)
    return preprocess_leaderboard(public_leaderboard)

def fetch_local_leaderboard(competition_name):
    with open(f'data/{competition_name}.json', 'r') as f:
        leaderboard = json.load(f)
    return leaderboard

def get_leaderboards() -> list[Leaderboard]:
    leaderboards = []
    for competition in COMPETITIONS:
        if competition['active']:
            if competition['type'] == 'online':
                leaderboards.append(Leaderboard(competition=competition['name'], teams=fetch_public_leaderboard(competition['name'])))
            elif competition['type'] == 'local':
                leaderboards.append(Leaderboard(competition=competition['name'], teams=fetch_local_leaderboard(competition['name'])))
    return leaderboards

def calculate_rank_score(rank, score, type='exponential'):
    if score < 0:
        return 0
    if type == 'linear':
        return 1 / rank
    elif type == 'exponential':
        return np.exp(-rank/4)

def sort_leaderboard(leaderboard):
    return sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

def get_datathon_leaderboard():
    leaderboards = get_leaderboards()
    datathon_leaderboard = {}
    for leaderboard in leaderboards:
        competition_coef = get_competition_coef(leaderboard.competition)
        for i, team in enumerate(leaderboard.teams):
            if team.name in datathon_leaderboard.keys():
                datathon_leaderboard[team.name] += competition_coef * calculate_rank_score(i+1, team.score)
            else:
                datathon_leaderboard[team.name] = competition_coef * calculate_rank_score(i+1, team.score)
    return preproces_datathon_leaderboard(sort_leaderboard(datathon_leaderboard))

if __name__ == '__main__':
    print(get_datathon_leaderboard())
                

    