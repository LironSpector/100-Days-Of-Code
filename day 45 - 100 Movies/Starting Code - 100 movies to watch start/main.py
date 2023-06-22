import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movies_text = []
for title in reversed(all_movies):
    with open("movies.txt", mode="a") as movies_file:
        movies_file.write(f"{title.getText()}\n")
