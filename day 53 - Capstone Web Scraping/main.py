import requests
from bs4 import BeautifulSoup

FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSf5BjXqmg0EmQWUZwYi9VywCB4FgggGo9AID9p-UurC5O1hyQ/viewform"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.884030776813404%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.666392961164114%2C%22west%22%3A-122.63417331103516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

response = requests.get(ZILLOW_URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
# print(soup)
# all_prices = soup.select(selector="span")
# all_link_elements = soup.find_all(name="img", class_="Image-c11n-8-73-8__sc-1rtmhsc-0 emzIcX")

# print(all_prices)
