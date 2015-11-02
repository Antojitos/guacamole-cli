import unittest
import sys

import requests_mock

from guacamole_cli import main as guacamole_cmd
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


class GuacamoleCMDTest(unittest.TestCase):

    def setUp(self):
        self.endpoint = 'http://localhost/files/'
        self.filename = 'test-image.jpg'
        self.filepath = 'tests/fixtures/%s' % self.filename

    def test_cmd_without_options(self):
        with self.assertRaises(SystemExit) as cm:
            guacamole_cmd()
        self.assertEqual(cm.exception.code, 2)

    def test_cmd_help(self):
        with self.assertRaises(SystemExit) as cm:
            args = ['--help']
            guacamole_cmd(args)
        self.assertEqual(cm.exception.code, 0)
        self.assertIn('show this help message and exit', sys.stdout.getvalue())

    def test_cmd_endpoit_fail(self):
        args = ['--endpoint', self.endpoint, self.filepath]
        output = guacamole_cmd(args)
        self.assertIn('something wrong with the endpoint', output)


if __name__ == '__main__':
    unittest.main(buffer=True)
