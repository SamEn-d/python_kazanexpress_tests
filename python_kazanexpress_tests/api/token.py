import os
import requests


usernameAPI = os.getenv('usernameAuth')
passwordAPI = os.getenv('passwordAuth')
APIURL = os.getenv('APIURL')


headers = {"authorization": "Basic a2F6YW5leHByZXNzLWN1c3RvbWVyOmN1c3RvbWVyU2VjcmV0S2V5",}


json_data = {
    "grant_type": "password",
    "username": usernameAPI,
    "password": passwordAPI,
}


def api_token():
    api_request = requests.post(APIURL + 'api/oauth/token/', data=json_data, headers=headers)
    return api_request.json()['access_token']
