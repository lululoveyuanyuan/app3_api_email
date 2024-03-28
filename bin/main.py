import requests

api_key = "6dfffb3abadd48baa056f83dbca0e4e6"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=6dfffb3abadd48baa056f83dbca0e4e6"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["descriptions"])
