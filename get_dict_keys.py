import requests

response = requests.get("https://api.github.com/repos/bpineda/flask-empty-app/pulls")

#print(response)
data = response.json()

for key in data[0]:
    print(key)

