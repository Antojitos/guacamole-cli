# Guacamole command line interface

A command line interface for https://github.com/Antojitos/guacamole

Tested with Python 2.7 and 3.4

[![Build Status](https://travis-ci.org/pabluk/guacamole-cli.svg)](https://travis-ci.org/pabluk/guacamole-cli)

## Install

```
$ pip install https://github.com/pabluk/guacamole-cli/archive/0.1.zip
```

## Usage

### Uploading a file
To upload a file you need to specify your Guacamole server URL and a filename, for example:
```
$ guacamole --endpoint http://guacamole-server/files/ screenshot.jpg
http://guacamole-server/files/TRPm/0lkq/6egk/yHgg/OeDg/fVHr/screenshot.jpg
```

### Command options
Use `--help` to show the command options:
```
$ guacamole --help
usage: guacamole [-h] [-c CONFIG_FILE] [-e ENDPOINT] filename

positional arguments:
  filename              file to upload

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_FILE, --config-file CONFIG_FILE
                        Specify a configuration file
  -e ENDPOINT, --endpoint ENDPOINT
                        Guacamole endpoint URL
```

## Configuration file
By default the command line interface looks for a configuration file in
`~/.guacamole.conf`. You can also specify an alternative configuration
file using the `--config-file` command line option.

Here's an example:
```
[general]
endpoint = http://guacamole.antojitos.io/files/
```

## Tests

In order to execute the test suite you need to run the next commands:
```
pip install -r requirements-dev.txt
```
```
python tests/main.py
```
