import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

movie_titles = soup.findAll(name="h3", class_="title")

with open("movies.txt", mode="w") as file:
    for title in movie_titles[::-1]:
        file.write(title.getText() + "\n")
