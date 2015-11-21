import json
import requests


class GuacamoleClient():
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def send(self, filename):
        files = {'file': open(filename, 'rb')}

        try:
            request = requests.post(self.endpoint, files=files)
        except requests.exceptions.RequestException:
            return
        response = request.json()
        if 'uri' in response:
            return '{0}{1}'.format(self.endpoint, response['uri'])


class TamalesClient():
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def shorten(self, url):
        data = json.dumps({'url': url})
        headers = {'Content-type': 'application/json'}

        try:
            request = requests.post(self.endpoint, data=data, headers=headers)
        except requests.exceptions.RequestException:
            return

        try:
            response = request.json()
        except ValueError:
            return

        if 'short_url' in response:
            return response['short_url']
