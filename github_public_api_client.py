import requests
from rich.console import Console

class GitHubPublicAPIClient:
    API_URL = "https://api.github.com/"
    console = Console()

    def callAPI(self, method_name):
        data = None
        try:
            response = requests.get(f"{self.API_URL}{method_name}")
            response.raise_for_status()

            if response.status_code != 200:
                print(response.status_code)
            data = response.json()

        except requests.exceptions.HTTPError as http_err:
            self.console.print(f'[red] {http_err} [/red]')

        return data

    def getPRS(self, repo_name):
        return self.callAPI(f"/repos/{repo_name}/pulls")

    def showResponseNodeNames(self, repo_name):
        data = self.callAPI(f"/repos/{repo_name}/pulls")
        for key in data[0]:
            print(key)


# Usage example
# client = GitHubPublicAPIClient()
# data = client.getPRS("bpineda/flask-empty-app")
# print(data)
