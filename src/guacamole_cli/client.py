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
