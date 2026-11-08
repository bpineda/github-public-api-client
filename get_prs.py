import requests
from rich.console import Console
from rich.table import Table

console = Console()
console.print("[blue]Type the name of the {user}/{repo} to get all of their PRs[/blue]")
console.print("e.g. [bold][yellow] docker/docs [/yellow][/bold] or [bold][yellow]PHPOffice/PHPPresentation[/yellow][/bold] or [bold][yellow]bpineda/flask-empty-app[/yellow][/bold]")
console.print("Constraint: the repo must be public")

repo_input = input()

data = ""
try:
    response = requests.get(f"https://api.github.com/repos/{repo_input}/pulls")
    response.raise_for_status()

    if response.status_code != 200:
        print(response.status_code)
    data = response.json()

except requests.exceptions.HTTPError as http_err:
    console.print(f'[red] {http_err} [/red]')

table = Table(title="Pull Requests")
columns = ["Title", "Author", "Status", "URL"]
for column in columns:
    table.add_column(column)

rows = []
for repo in data:
    table.add_row(repo['title'], repo['user']['login'], repo['state'], repo['html_url'], style='bright_yellow')

console.print(table)
