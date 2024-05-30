import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime

load_dotenv()

def get_total_public_repos():
    access_token = os.getenv('GITHUB_API')
    
    # GitHub API URL for searching repositories
    url = 'https://api.github.com/search/repositories?q=is:public'
    
    headers = {}
    if access_token:
        headers['Authorization'] = f'token {access_token}'

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        total_count = data['total_count']
        print(f"Total number of public repositories: {total_count}")

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        # Dump data to a file
        with open(f'github_repo_{timestamp}.json', 'w') as f:
            json.dump(data, f, indent=4)
    else:
        print("Failed to fetch data", response.status_code)

get_total_public_repos()
