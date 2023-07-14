import data
import requests
import configuration

def post_new_orders():
    response = requests.post(configuration.URL + configuration.CREATE_ORDERS_PATH,
                             json=data.body)
    return response.json()["track"]

def new_track():
    return str(post_new_orders())
def get_orders_track():
    response = requests.get(configuration.URL + configuration.GET_ORDERS_PATH_TRACK + new_track())
    return response

