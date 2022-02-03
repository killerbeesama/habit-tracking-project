import requests

name = "<your name>"

PIXELA_ENDPOINT = "<your endpoint>"

API_KEY = "<your api key>"

##------------------------------------------ CREATE A USER --------------------------------------------------##
parameter = {
    "token": API_KEY,
    "username": name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#
# r = requests.post(url=PIXELA_ENDPOINT, json=parameter)
# data = r.text
# print(data)

##------------------------------------------ CREATE A GRAPH ------------------------------------------------##

GRAPH_ID = "graph1"

PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{name}/graphs"

graph_parameter = {
    "id": GRAPH_ID,
    "name": "exp-graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": API_KEY,
}

# r = requests.post(url=PIXELA_GRAPH_ENDPOINT, headers=headers, json=graph_parameter)
# data = r.text
# print(data)

##------------------------------------------ POST A PIXEL ------------------------------------------------##

PIXELA_POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{name}/graphs/{GRAPH_ID}"

post_parameter = {
    "date": "<your date as string eg--20211230>",
    "quantity": "<your number>",
}

# r = requests.post(url=PIXELA_POST_PIXEL_ENDPOINT, headers=headers, json=post_parameter)
# data = r.text
# print(data)
