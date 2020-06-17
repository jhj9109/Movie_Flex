import requests
import json
from pprint import pprint
from decouple import config

TMDB_URL = 'https://api.themoviedb.org/3/movie/popular'
BASIC_IMG_URL = 'https://image.tmdb.org/t/p/w500'
API_KEY = config('TMDB_API_KEY')


total_movie_list = []
for i in range(1, 501): # 데이터 받아오는 개수 1당 => 20개
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

    # 데이터가 없는아이들은 추가안해줌
    # 개봉일 없어서 KeyError 나와서 get 함수로 잠시 바꿈
    if movie.get('release_date') == None:
        continue
    else:
        fields['release_date'] = movie.get('release_date')

    if movie.get('poster_path') == None:
        continue
    else:
        fields['poster_path'] = BASIC_IMG_URL + movie.get('poster_path')

    if movie.get('backdrop_path') == None:
        continue
    else:
        fields['backdrop_path'] = BASIC_IMG_URL + movie.get('backdrop_path')

    fields['adult'] = movie['adult']
    fields['vote_average'] = movie['vote_average']
    fields['genre'] = movie['genre_ids']

    inner['fields'] = fields

    result.append(inner)


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent="\t")
