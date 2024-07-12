import requests
import csv
from random import choice
from bs4 import BeautifulSoup


def write_to_file(content):
    with open("./top_100_movies.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow("movie_name,description_link")
        for row in content:
            writer.writerow(row)

def scrap_movies_from_web():
    link = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
    response = requests.get(link)
    if response.status_code == 200:
        web_content = response.text
    else:
        print("Something's wrong with endpoint. Connection status code: ", response.status_code)
    soup = BeautifulSoup(web_content, "html.parser")
    movies_raw = soup.select(".entity-info-items__list li a")
    movies = [(movie.getText(), movie.get("href")) for movie in movies_raw]
    return movies

def pick_random_movie(movies_list):
    """ Pick one of given movies to watch
    """
    movie = choice(movies_list)
    print(f"Your movie for tonight is {movie[0]}!\n Link for description is given here: {movie[1]}\n\tEnjoy the show!") 

def main():
    movies_list = scrap_movies_from_web()
    write_to_file(movies_list)
    pick_random_movie(movies_list)


if __name__ == "__main__":
    main()