import requests
from rich.console import Console
from rich.table import Table

from github_public_api_client import GitHubPublicAPIClient

console = Console()
console.print("[blue]Type the name of the {user}/{repo} to get all of their PRs[/blue]")
console.print("e.g. [bold][yellow] docker/docs [/yellow][/bold] or [bold][yellow]PHPOffice/PHPPresentation[/yellow][/bold] or [bold][yellow]bpineda/flask-empty-app[/yellow][/bold]")
console.print("Constraint: the repo must be public")

repo_input = input()

client = GitHubPublicAPIClient()
data = client.getPRS(repo_input)


table = Table(title="Pull Requests")
columns = ["Title", "Author", "Status", "URL"]
for column in columns:
    table.add_column(column)

rows = []
if data == None:
    console.print("[yellow]No values[/yellow]")
else:
    for repo in data:
        table.add_row(repo['title'], repo['user']['login'], repo['state'], repo['html_url'], style='bright_yellow')

    console.print(table)
