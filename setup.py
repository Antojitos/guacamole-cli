from setuptools import setup, find_packages


with open('README.rst') as file:
    long_description = file.read()


setup(
    name="guacamole-cli",
    version="0.3.1",
    author="Pablo SEMINARIO",
    author_email="pablo@seminar.io",
    description="Guacamole command line interface",
    long_description=long_description,
    license="GNU General Public License v3 (GPLv3)",
    url="https://github.com/Antojitos/guacamole-cli",
    download_url="https://github.com/Antojitos/guacamole-cli/archive/0.3.1.tar.gz",
    keywords=["cli", "guacamole"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],

    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'guacamole = guacamole_cli:main',
        ]
    },
    install_requires=['requests'],
)
