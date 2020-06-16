import requests
import json
from pprint import pprint
from decouple import config

TMDB_URL = 'https://api.themoviedb.org/3/movie/popular'
BASIC_IMG_URL = 'https://image.tmdb.org/t/p/w500'
API_KEY = config('WEATHER_API_KEY')


total_movie_list = []
for i in range(1, 6): # 데이터 받아오는 개수 1당 => 20개
    Params = {
        'api_key': API_KEY,
        'language': 'ko',
        'page': i,
    }
    movie_list = requests.get(TMDB_URL, Params).json()['results']
    total_movie_list.extend(movie_list)

result = []
for movie in total_movie_list:
    inner = {}
    inner["model"] = 'movies.movie'
    inner["pk"] = movie['id']

    fields = {}

    fields['title'] = movie['title']
    fields['title_en'] = movie['original_title']
    fields['overview'] = movie['overview']
    fields['release_date'] = movie['release_date']

    fields['poster_path'] = BASIC_IMG_URL + movie['poster_path']
    fields['backdrop_path'] = BASIC_IMG_URL + movie['backdrop_path']

    fields['adult'] = movie['adult']
    fields['vote_average'] = movie['vote_average']
    fields['genre'] = movie['genre_ids']

    inner['fields'] = fields

    result.append(inner)


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent="\t")
