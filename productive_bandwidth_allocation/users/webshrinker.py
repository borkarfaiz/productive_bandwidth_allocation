import hashlib
import json
from base64 import urlsafe_b64encode
from urllib.parse import urlencode

import requests


def webshrinker_categories_v3(access_key, secret_key, url=b"", params={}):
    params['key'] = access_key

    request = "categories/v3/{}?{}".format(urlsafe_b64encode(url).decode('utf-8'), urlencode(params, True))
    request_to_sign = "{}:{}".format(secret_key, request).encode('utf-8')
    signed_request = hashlib.md5(request_to_sign).hexdigest()

    return "https://api.webshrinker.com/{}&hash={}".format(request, signed_request)


access_key = "YF7PC6AHWLuteCAMVtRh"
secret_key = "uEdKIBhKMmfmtbspS6J5"

url = b"https://docs.djangoproject.com/en/2.0/"

api_url = webshrinker_categories_v3(access_key, secret_key, url)
response = requests.get(api_url)

status_code = response.status_code
data = response.json()

if status_code == 200:
    # Do something with the JSON response
    print(json.dumps(data, indent=4, sort_keys=True))
elif status_code == 202:
    # The website is being visited and the categories will be updated shortly
    print(json.dumps(data, indent=4, sort_keys=True))
elif status_code == 400:
    # Bad or malformed HTTP request
    print("Bad or malformed HTTP request")
    print(json.dumps(data, indent=4, sort_keys=True))
elif status_code == 401:
    # Unauthorized
    print("Unauthorized - check your access and secret key permissions")
    print(json.dumps(data, indent=4, sort_keys=True))
elif status_code == 402:
    # Request limit reached
    print("Account request limit reached")
    print(json.dumps(data, indent=4, sort_keys=True))
else:
    # General error occurred
    print("A general error occurred, try the request again")
