url = "https://www.cars24.com/ae/buy-used-cars-dubai/"

import requests
from bs4 import BeautifulSoup

response = requests.get(url)
print(response.status_code)
print(len(response.text))
doc = BeautifulSoup(response.text, "html.parser")
print(len(doc))
