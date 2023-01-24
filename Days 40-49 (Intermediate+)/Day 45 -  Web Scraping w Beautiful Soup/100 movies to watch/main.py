from math import e
from operator import mod
from urllib import response
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
# response = requests.get(URL)
# web_html = response.text
# soup = BeautifulSoup(web_html, "html.parser")
# movies_tag = soup.find_all(name="h3", class_="title")
# movies_list = [movie.getText().split(") ") for movie in movies_tag]
# erro = movies_list[-12][0].split(": ")
# movies_list.insert(-12, erro)
# movies_list.remove(['12: The Godfather Part II'])
# dict_movies = {int(filme[0]):filme[1] for filme in movies_list}
# with open("lista_filmes.txt", "w", encoding="utf-8")as writer:
#     for key, val in reversed(dict_movies.items()):
#         writer.write(f"{key}) {val}\n")


    
# ******************* Correção ************************* #
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")