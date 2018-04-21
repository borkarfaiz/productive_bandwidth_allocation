import hashlib
import json
from base64 import urlsafe_b64encode
from urllib.parse import urlencode

import pandas as pd
import requests

from .users_classification import DATA_PATH

data = pd.read_csv(DATA_PATH + r'\webshrinkerkeys.csv', header=None, index_col=False,
                   names=['E-mail ID',
                          'access_key',
                          'secret_key',
                          'remaining_attempts'])


def classify_url(url):
    user_info = get_info()
    api_url = web_shrinker_categories_v3(user_info.access_key.to_string(index=False),
                                         user_info.secret_key.to_string(index=False), url=url)
    response = requests.get(api_url)
    user_info.remaining_attempts -= 1
    status_code = response.status_code
    json_data = response.json()

    if status_code == 200:
        # Do something with the JSON response
        print(json.dumps(json_data, indent=4, sort_keys=True))
    elif status_code == 202:
        # The website is being visited and the categories will be updated shortly
        print(json.dumps(json_data, indent=4, sort_keys=True))
    elif status_code == 400:
        # Bad or malformed HTTP request
        print("Bad or malformed HTTP request")
        print(json.dumps(json_data, indent=4, sort_keys=True))
    elif status_code == 401:
        # Unauthorized
        print("Unauthorized - check your access and secret key permissions")
        print(json.dumps(json_data, indent=4, sort_keys=True))
    elif status_code == 402:
        # Request limit reached
        print("Account request limit reached")
        print(json.dumps(json_data, indent=4, sort_keys=True))
    else:
        # General error occurred
        print("A general error occurred, try the request again")
    update_info(user_info)
    for information in json_data['data']:
        for categories in information['categories']:
            return categories['label']


def web_shrinker_categories_v3(access_key, secret_key, url=b"", params={}):
    params['key'] = access_key

    request = "categories/v3/{}?{}".format(urlsafe_b64encode(url).decode('utf-8'), urlencode(params, True))
    request_to_sign = "{}:{}".format(secret_key, request).encode('utf-8')
    signed_request = hashlib.md5(request_to_sign).hexdigest()

    return "https://api.webshrinker.com/{}&hash={}".format(request, signed_request)


def get_info():
    for i in range(len(data)):
        user_info = data.loc[i]
        if user_info.remaining_attempts > 0:
            return data.loc[data['access_key'] == user_info.access_key]
    raise Exception('All Tokens Have been used')


def update_info(user_info):
    data._set_value(user_info.index, 'remaining_attempts', user_info.remaining_attempts)
    data.to_csv(DATA_PATH + r'\webshrinkerkeys.csv', header=False, index=False)
