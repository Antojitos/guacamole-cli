import argparse

from guacamole_cli.client import GuacamoleClient


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--endpoint', help='Guacamole endpoint URL',
                        default='http://localhost/files/')
    parser.add_argument('filename', help='file to upload')
    args = parser.parse_args()

    client = GuacamoleClient(args.endpoint)
    url = client.send(args.filename)
    if url:
        print(url)
    else:
        error_msg = 'Oops! It seems there\'s something wrong with {0}'
        print(error_msg.format(args.endpoint))
