import requests
from time import sleep

def delete_repositories(token_key, repos_list):
    """Delete GitHub repositories listed in repos_list."""
    url = "https://api.github.com/repos/{}/{}"
    
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token_key}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    for line in repos_list:
        # Skip empty lines and comments
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        try:
            owner, repo = line.split("/")
        except ValueError:
            print(f"ERROR: Invalid repository format: {line}")
            continue
        
        full_url = url.format(owner, repo)
        print(f"Deleting repository: {full_url}")
        
        try:
            response = requests.delete(url=full_url, headers=headers)
            if response.status_code == 204:
                print(f"Successfully deleted repository: {full_url}")
            else:
                print(f"Failed to delete repository: {full_url}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for repository: {full_url}. Error: {e}")
        
        # Sleep to avoid hitting rate limits
        sleep(2)

if __name__ == '__main__':
    # GitHub token with delete permissions
    delete_repo_token = "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"
    
    # Path to the file containing the list of repositories
    file_path = './repos.txt'
    
    # Read the repository list from the file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.readlines()
    except IOError as e:
        print(f"ERROR: Unable to read file {file_path}. Error: {e}")
        exit(1)
    
    # Delete the repositories
    delete_repositories(delete_repo_token, data)
    
    print("Finished.")