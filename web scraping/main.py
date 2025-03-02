import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response=requests.get(URL)
page=response.text

soup=BeautifulSoup(page,"html.parser")

film=soup.find_all(name="h3",class_="title")
film_name=[]

for i in film:
    f_name=i.getText()
    film_name.append(f_name)
    

movie=film_name[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for i in movie:
        file.write(f"{i}\n")

