import sys
import requests
from bs4 import BeautifulSoup

input = sys.argv[1]
add = "http://"
url = add + input
req = requests.get(url)

retrieve = BeautifulSoup(req.text, 'html.parser')

print("Title of page: ")
for title in retrieve.find_all("title"):
    print(title.get_text())
