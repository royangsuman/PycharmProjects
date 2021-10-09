import requests
import json
from requests.auth import HTTPBasicAuth

def test_basicAu():
    response = requests.get('https://api.github.com/user',auth=HTTPBasicAuth('angsuma1010','$'))
    print(response.text)