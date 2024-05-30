import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime

load_dotenv()

def get_top_repos():
    access_token = os.getenv('GITHUB_API')

    # GitHub API URL for searching repositories
    url = 'https://api.github.com/search/repositories?q=is:public&sort=stars&order=desc'

    headers = {}
    if access_token:
        headers['Authorization'] = f'token {access_token}'

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        repos = data['items']

        # Sort repos by star counts and get top 20
        top_20_star_repos = sorted(repos, key=lambda repo: repo['stargazers_count'], reverse=True)[:20]

        # Get repo names and star counts
        repo_names_star = [repo['full_name'] for repo in top_20_star_repos]
        star_counts = [repo['stargazers_count'] for repo in top_20_star_repos]

        # Sort repos by fork counts and get top 20
        top_20_fork_repos = sorted(repos, key=lambda repo: repo['forks_count'], reverse=True)[:20]

        # Get repo names and fork counts
        repo_names_fork = [repo['full_name'] for repo in top_20_fork_repos]
        fork_counts = [repo['forks_count'] for repo in top_20_fork_repos]

        # Create a dictionary to store repo names and star counts
        star_dict = {repo['full_name']: repo['stargazers_count'] for repo in top_20_star_repos}

        # Create a dictionary to store repo names and fork counts
        fork_dict = {repo['full_name']: repo['forks_count'] for repo in top_20_fork_repos}

        # Combine the two dictionaries
        combined_dict = {'Top 20 Star Repos': star_dict, 'Top 20 Fork Repos': fork_dict}

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        # Dump data to a file
        with open(f'github_top20_repo_{timestamp}.json', 'w') as f:
            json.dump(combined_dict, f, indent=4)

    else:
        print("Failed to fetch data", response.status_code)

get_top_repos()