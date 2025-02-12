# GitHub Repository Cleanup Tool

This project provides a simple Python script to list and delete GitHub repositories in bulk. It is designed to help users manage their GitHub repositories more efficiently, especially when dealing with a large number of repositories.

## Features

- **List Repositories**: Fetches all repositories owned by the authenticated user and saves them to a file (`repos.txt`).
- **Delete Repositories**: Reads a list of repositories from `repos.txt` and deletes them one by one using the GitHub API.

## Prerequisites

- Python 3.x
- A GitHub Personal Access Token (PAT) with the `repo` scope.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/github-repo-cleanup.git
   cd github-repo-cleanup
   ```

2. **Install Dependencies**:
   ```bash
   pip install requests
   ```

3. **Set Up Your GitHub Token**:
   - Generate a GitHub Personal Access Token (PAT) with the `repo` scope from [GitHub Developer Settings](https://github.com/settings/tokens).
   - Replace the placeholder token in both `list_gitlab_repository.py` and `delete_gitlab_repositories.py` with your actual token.

## Usage

### 1. Listing Repositories

To list all repositories owned by the authenticated user and save them to `repos.txt`, run:

```bash
python list_gitlab_repository.py
```

This script will:
- Fetch all repositories from GitHub.
- Save the repository names in the format `owner/repo` to `repos.txt`.
- Print the repository names and URLs to the console.

### 2. Deleting Repositories

To delete repositories listed in `repos.txt`, run:

```bash
python delete_gitlab_repositories.py
```

This script will:
- Read the list of repositories from `repos.txt`.
- Delete each repository one by one using the GitHub API.
- Print the status of each deletion attempt.

### File Format (`repos.txt`)

The `repos.txt` file should contain one repository per line in the format `owner/repo`. Lines starting with `#` are treated as comments and will be ignored.

Example:
```plaintext
# 用户名/仓库名
dualseason/3d
dualseason/likeshop
dualseason/LMSpaceDev
```

## Notes

- **Rate Limiting**: The script includes a 2-second delay between deletion requests to avoid hitting GitHub's rate limits.
- **Error Handling**: The script handles common errors such as invalid repository formats and network issues.
- **Backup**: Ensure you have a backup of any important repositories before running the deletion script.

## References

- [GitHub API Documentation](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#delete-a-repository)
- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

**Disclaimer**: Use this tool at your own risk. Deleting repositories is irreversible. Make sure you have backups of any important data before proceeding.