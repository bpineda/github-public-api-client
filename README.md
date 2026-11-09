# Github Public API client

This is an example of how to consume the GitHub public API.

Usage:

## Setup the environment

```
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```
## Usage example

```
client = GitHubPublicAPIClient()
data = client.getPRS("bpineda/flask-empty-app")
print(data)
```
