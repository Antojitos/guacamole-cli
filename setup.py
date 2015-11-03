from setuptools import setup, find_packages


setup(
    name="guacamole-cli",
    version="0.2.0",
    author="Pablo SEMINARIO",
    author_email="pablo@seminar.io",
    description="Guacamole command line interface",
    license="GPLv3",
    keywords="cli guacamole",
    url="https://github.com/pabluk/guacamole-cli",

    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'guacamole = guacamole_cli:main',
        ]
    },
    install_requires=['requests'],
)
