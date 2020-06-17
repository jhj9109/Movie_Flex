from django.test import TestCase

import requests
# Create your tests here.


# http://openweathermap.org/img/wn/10d@2x.png [이미지 URL]
# https://openweathermap.org/weather-conditions [wheather 컬럼정보]
def get_weather(data):
    API_KEY = 'a33f66615c22bc4a01086192ca00ac4c'
    city_name = 'Seoul'
    if data:
        lat, lon = data
        API_URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    else:
        API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

    res = requests.get(API_URL).json()
    weather = res['weather'][0]['main']
    img = res['weather'][0]['icon']
    IMG_URL = f'http://openweathermap.org/img/wn/{img}@2x.png'
    loc_name = res['name'] #도시명

    return weather, IMG_URL, loc_name

def recommend_movie(params):
    print(f'___recommend_movie____시작')
    if params['code']:
        weather, IMG_URL, loc_name = get_weather((params['lat'], params['lon']))
        print('___유저 정보 사용____')
    else:
        weather, IMG_URL, loc_name = get_weather(None) # wheather = ['Clear', 'Clouds', 'Rain', 'Tornado', '']
        print('____디폴트 값 사용____')

    # 테스트코드 ( 날씨와 이미지 바꾸고 싶을 때 잠시 테스트용 코드 )
    # weather = 'Clear'
    # IMG_URL = 'http://openweathermap.org/img/wn/10n@2x.png'

    if weather == 'Thunderstorm':
        return ['Horror', 'Crime', 'Thriller', 'Mystery'], IMG_URL, loc_name
    elif weather == 'Drizzle':
        return ['Drama', 'Animation', ], IMG_URL, loc_name
    elif weather == 'Rain':
        return ['Romance', 'Music', 'Animation'], IMG_URL, loc_name
    elif weather == 'Snow':
        return ['Fantasy', 'Family', 'Science Fiction'], IMG_URL, loc_name
    elif weather == 'Clear':
        return ['Adventure', 'Action', 'Comedy'], IMG_URL, loc_name
    elif weather == 'Clouds':
        return ['TV Movie', 'War'], IMG_URL, loc_name
    else: # Atmosphere
        return ['History', 'Western', 'Documentary'], IMG_URL, loc_name



