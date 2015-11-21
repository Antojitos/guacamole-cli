import argparse
import os.path

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from guacamole_cli.client import GuacamoleClient
from guacamole_cli.client import TamalesClient


CONFIG_FILE = os.path.join(os.path.expanduser('~'), '.guacamole.conf')


def get_settings(config_file):
    """Search and load a configuration file."""
    default_settings = {
        'general': {'endpoint': '', 'shortener': ''}
    }

    settings = configparser.ConfigParser()
    try:
        settings.read_dict(default_settings)
    except AttributeError:
        # using python 2.7
        for section, options in default_settings.items():
            settings.add_section(section)
            for option, value in options.items():
                settings.set(section, option, value)

    if config_file is not None and os.path.exists(config_file):
        settings.read(config_file)
        return settings
    if os.path.exists(CONFIG_FILE):
        settings.read(CONFIG_FILE)
        return settings
    return settings


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config-file',
                        help='Specify a configuration file')
    parser.add_argument('-e', '--endpoint',
                        help='Guacamole endpoint URL')
    parser.add_argument('-s', '--shortener',
                        help='Tamales endpoint URL')
    parser.add_argument('filename',
                        help='file to upload')
    args = parser.parse_args(args)

    settings = get_settings(args.config_file)

    endpoint = args.endpoint or settings.get('general', 'endpoint')
    shortener = args.shortener or settings.get('general', 'shortener')

    if not endpoint:
        error_msg = 'You must specify an endpoint URL using the --endpoint ' \
                    'command option or via the a configuration file by ' \
                    'default in {0}'.format(CONFIG_FILE)
        return error_msg

    client = GuacamoleClient(endpoint)
    url = client.send(args.filename)
    if not url:
        error_msg = 'Oops! It seems there\'s something wrong ' \
                    'with the endpoint {0}'.format(endpoint)
        return error_msg

    if shortener:
        client = TamalesClient(shortener)
        url = client.shorten(url)
        if not url:
            error_msg = 'Oops! It seems there\'s something wrong ' \
                        'with the URL shortener service {0}'.format(shortener)
            return error_msg
        print(url)
    else:
        print(url)
