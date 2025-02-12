import requests

def list_github_repositories():
    url = "https://api.github.com/user/repos"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer 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",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repositories = response.json()
        with open('repos.txt', 'a') as f:
            for repo in repositories:
                repo_name = repo['name']
                repo_owner = repo['owner']['login']
                f.write(f"{repo_owner}/{repo_name}\n")
                print(f"Repository Name: {repo_name}, URL: {repo['html_url']}")
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")

if __name__ == "__main__":
    list_github_repositories()
