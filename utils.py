import requests

from models import Team

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
