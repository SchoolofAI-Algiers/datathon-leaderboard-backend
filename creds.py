import os
import dotenv
import json 
from pathlib import Path

dotenv.load_dotenv()

KAGGLE_USERNAME = os.getenv('KAGGLE_USERNAME')
KAGGLE_KEY = os.getenv('KAGGLE_KEY')

# def configure_credentials():
#     api_key = {
#         'username': KAGGLE_USERNAME,
#         'key': KAGGLE_KEY
#     }

#     kaggle_path = Path('/home/brouthen/.kaggle')
#     os.makedirs(kaggle_path, exist_ok=True)
    
#     with open (kaggle_path/'kaggle.json', 'w') as f:
#         json.dump(api_key, f)

#     os.chmod(kaggle_path/'kaggle.json', 777)
    
# configure_credentials()