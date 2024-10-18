def find_home_away(data):
    competitors = data['sport_event']['competitors']
    home_competitor = None
    away_competitor = None
    for competitor in competitors:
        if competitor['qualifier'] == 'home':
            home_competitor = competitor['name']
        elif competitor['qualifier'] == 'away':
            away_competitor = competitor['name']
    return home_competitor, away_competitor


def print_score(data, home_score, away_score):
    find_home_away(data)
    home_competitor = find_home_away(data)[0]
    away_competitor = find_home_away(data)[1]
    print(f"Competitor: {home_competitor}")
    print(f"Home Score: {home_score}")

    print(f"Competitor: {away_competitor}")
    print(f"Away Score: {away_score}")
