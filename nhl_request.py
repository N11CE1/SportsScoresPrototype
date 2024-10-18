import requests

import common

url = ("https://api.sportradar.com/australianrules/trial/v3/en/sport_events/sr%3Asport_"
       "event%3A53800561/timeline.json?api_key=zgAujIrS4hvb4163NzQrwh3gfHhuKL9w0E57ACOE")

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()

home_score = data['sport_event_status'].get('home_display_score')
away_score = data['sport_event_status'].get('away_display_score')
common.find_home_away(data)

home_competitor = common.find_home_away(data)[0]
away_competitor = common.find_home_away(data)[1]

# common.print_score(data, home_score, away_score)
