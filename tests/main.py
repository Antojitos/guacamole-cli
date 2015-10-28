import unittest

import requests_mock

from guacamole_cli.client import GuacamoleClient


class GuacamoleClientTest(unittest.TestCase):

    def setUp(self):
        self.endpoint = 'http://localhost/files/'
        self.filename = 'test-image.jpg'
        self.filepath = 'tests/fixtures/%s' % self.filename
        self.client = GuacamoleClient(self.endpoint)

    def test_client_send(self):
        with requests_mock.Mocker() as m:
            m.post(self.endpoint, text='{"uri": "h/a/s/h/%s"}' % self.filename)

            expected_url = 'http://localhost/files/h/a/s/h/test-image.jpg'
            received_url = self.client.send(self.filepath)
            self.assertEqual(expected_url, received_url)


if __name__ == '__main__':
    unittest.main()
