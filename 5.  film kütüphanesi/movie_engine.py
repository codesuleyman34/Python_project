from screen_support import *
movies = {}


def show_movies():
    for movie_key in movies.keys():
        name = movies[movie_key]["movie_name"]
        director = movies[movie_key]["movie_director"]
        year = movies[movie_key]["movie_year"]
        show_name_director_and_year(movie_key, name, director, year)

def add_movie():
    name = get_name()
    director = get_director()
    year = get_year()
    key = len(movies.items()) +1
    movies[key] = {"movie_name": name, "movie_director": director, "movie_year": year}

def delete_movie():
    movie_key = get_delete_movie()
    movies.pop(movie_key)