from django.test import TestCase

import requests
# Create your tests here.


# http://openweathermap.org/img/wn/10d@2x.png [이미지 URL]
# https://openweathermap.org/weather-conditions [wheather 컬럼정보]
def get_weather():
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q=Seoul&units=metric&appid=a33f66615c22bc4a01086192ca00ac4c&lang=kr'
    res = requests.get(API_URL).json()

    weather = res['weather'][0]['main']
    img = res['weather'][0]['icon']
    IMG_URL = f'http://openweathermap.org/img/wn/{img}@2x.png'

    # print('weather: ', weather)
    # print('IMG_URL: ', IMG_URL)
    return weather, IMG_URL


def recommend_movie():
    weather, IMG_URL = get_weather() # wheather = ['Clear', 'Clouds', 'Rain', 'Tornado', '']

    # 테스트코드 ( 날씨와 이미지 바꾸고 싶을 때 잠시 테스트용 코드 )
    # weather = 'Clear'
    # IMG_URL = 'http://openweathermap.org/img/wn/10n@2x.png'
    if weather == 'Thunderstorm':
        return ['Horror', 'Crime', 'Thriller', 'Mystery'], IMG_URL
    elif weather == 'Drizzle':
        return ['Drama', 'Animation', ], IMG_URL
    elif weather == 'Rain':
        return ['Romance', 'Music', 'Animation'], IMG_URL
    elif weather == 'Snow':
        return ['Fantasy', 'Family', 'Science Fiction'], IMG_URL
    elif weather == 'Clear':
        return ['Adventure', 'Action', 'Comedy'], IMG_URL
    elif weather == 'Clouds':
        return ['TV Movie', 'War'], IMG_URL
    else: # Atmosphere
        return ['History', 'Western', 'Documentary'], IMG_URL



