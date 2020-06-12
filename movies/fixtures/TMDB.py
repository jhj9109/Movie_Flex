import requests
from pprint import pprint
import json

TMDB_URL = 'https://api.themoviedb.org/3/movie/popular'
BASIC_IMG_URL = 'https://image.tmdb.org/t/p/w500'
API_KEY = '042b8288c71af382ae35655b0744652c'


total_movie_list = []
for i in range(1, 6):
    Params = {
        'api_key': API_KEY,
        'language': 'ko',
        'page': i,
    }
    movie_list = requests.get(TMDB_URL, Params).json()['results']
    total_movie_list.extend(movie_list)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(total_movie_list, f, indent="\t")
