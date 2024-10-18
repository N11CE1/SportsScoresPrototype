import requests

import common

url = ("https://api.sportradar.us/rugby-league/trial/v3/en/sport_events/"
       "sr%3Asport_event%3A45484084/summary.json?api_key=zgAujIrS4hvb4163NzQrwh3gfHhuKL9w0E57ACOE")

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()

home_score = data['sport_event_status'].get('home_score')
away_score = data['sport_event_status'].get('away_score')
common.find_home_away(data)

home_competitor = common.find_home_away(data)[0]
away_competitor = common.find_home_away(data)[1]

# common.print_score(data, home_score, away_score)
