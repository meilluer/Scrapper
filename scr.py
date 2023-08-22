
import requests
from bs4 import BeautifulSoup
req = requests.get("https://www.youtube.com/watch?v=4tAp9Lu0eDI")
soup = BeautifulSoup(req.content, "html.parser")

for link in soup.find_all("a")[0]:
      print(link.get("href"))