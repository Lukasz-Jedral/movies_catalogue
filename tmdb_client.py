import requests
from random import sample

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2OWFlZjE2NzgxNzdjNTE5MjBmOWRlYmEzMzIxOWRiNiIsInN1YiI6IjVmNTRlN2Y1MzUwMzk4MDAzMzgxMzA5NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jtmP7AzbjryJze2GaPQ2Is-ZtYhzFGkZ6BYTBYfDURQ"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]
