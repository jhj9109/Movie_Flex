from django.test import TestCase

import requests
# Create your tests here.

# https://openweathermap.org/weather-conditions [wheather 컬럼정보]
def get_weather():
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q=Seoul&units=metric&appid=a33f66615c22bc4a01086192ca00ac4c&lang=kr'
    res = requests.get(API_URL).json()

    온도 = res['main']['temp']
    습도 = res['main']['humidity']
    날씨 = res['weather'][0]['main']
    print(온도, 습도, 날씨)
    return 온도, 습도, 날씨

def recommend_movie():
    temp, h, weather = get_weather() # wheather = ['Clear', 'Clouds', 'Rain', 'Tornado', '']
    # 덥고 습할때,,
    if temp > 30 or h > 75:
        return ['Fantasy', 'Horror', 'Thriller', 'Mystery']

    # 날씨 (맑음, 흐림, 비, 눈) => 장르 n개 => random 1개 장르 추천 => 흐린 오늘 같은날에 Action 영화어떄요? / 흐린 오늘 같은날엔 감성적인 멜로와 함께 추천합니다?
    # 흐린 날씨의 초이스 액션! / 흐린 날씨의 초이스 멜로!
    weather =



