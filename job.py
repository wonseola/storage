import requests
from bs4 import BeautifulSoup

url = "https://remoteok.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

jobs = soup.find("div",class_="container").find_all("a")

