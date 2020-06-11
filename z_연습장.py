import requests

movie_api = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.json'
params = {
    'key': 'df6858465977b699d39998ff138c3344',
}

res = requests.get(movie_api, params)

print(res.__dir__())
