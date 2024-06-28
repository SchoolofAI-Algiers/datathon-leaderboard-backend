import requests

from models import Team
from config import COMPETITIONS

def get_competition_by_name(name):
    for competition in COMPETITIONS:
        if competition['name'] == name:
            return competition
    return None

def get_competition_coef(name):
    competition = get_competition_by_name(name)
    return competition['coef'] if competition else None

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Failed to fetch the HTML content. Status code: {e.response.status_code}")
        raise e
    
def preprocess_team(team: dict):
    return Team(name=team['teamName'], score=team['score'])

def preprocess_leaderboard(leaderboard):
    return [preprocess_team(team) for team in leaderboard['submissions']]

def preproces_datathon_leaderboard(leaderboard):
    return [Team(name=team[0], score=float(f"{team[1]:.2f}")) for team in leaderboard]
