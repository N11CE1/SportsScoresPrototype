import requests
import pandas as pd

baseurl = "https://rickandmortyapi.com/api/"

endpoint = "character"


def main_request(base_url, end_point, a):
    r = requests.get(base_url + end_point + f"?page={a}")
    return r.json()


def get_pages(response):
    return response["info"]["pages"]


def parse_json(response):
    char_list = []
    for item in response["results"]:
        char = {
            "ID": item["id"],
            "name": item["name"],
            "no_ep": len(item["episode"]),
        }

        char_list.append(char)
    return char_list


main_list = []
data = main_request(baseurl, endpoint, 1)
for x in range(1, get_pages(data) + 1):
    print(x)
    main_list.extend(parse_json(main_request(baseurl, endpoint, x)))

df = pd.DataFrame(main_list)

df.to_csv("charlist.csv", index=False)
