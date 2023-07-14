import data
import requests
import configuration

def post_new_orders():
    response = requests.post(configuration.URL + configuration.CREATE_ORDERS_PATH,
                             json=data.body)
    return response

def pull_out_track():
    response = requests.get(configuration.URL + configuration.GET_ORDERS_PATH)
    track = response.json()["orders"][0]["track"]
    return str(track)
def get_orders_track():
    response = requests.get(configuration.URL + configuration.GET_ORDERS_PATH_TRACK + pull_out_track())
    return response

