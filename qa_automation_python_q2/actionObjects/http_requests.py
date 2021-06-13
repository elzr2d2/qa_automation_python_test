import json

import requests
from utilities.convertJson import convertJson
from utilities.readProperties import ReadConfig


def create_token(username, password):
    url = ReadConfig.get_login_url()

    payload = json.dumps({
        "username": username,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()['access_token']
    return str(f"Bearer {token}")


def post_request(token, data):
    url = ReadConfig.get_application_url()

    payload = data
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return convertJson(response.json())


def get_request(token, object_id=None):
    if object_id:
        url = ReadConfig.get_application_url() + "/" + {object_id}
    else:
        url = ReadConfig.get_application_url()

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return convertJson(response.json())


def del_request(token, object_id):
    url = ReadConfig.get_application_url() + "/" + {object_id}

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return convertJson(response.json())
