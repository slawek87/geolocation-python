# -*- coding: utf-8 -*-
from distutils.core import setup

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE.txt', 'r') as f:
    license_ = f.read()

setup(
    name='geolocation-python',
    version='0.1.2c',
    packages=['geolocation'],
    url='',
    download_url='https://github.com/slawek87/geolocation-python/',
    license=license_,
    author=u'Sławomir Kabik',
    author_email='slawek@redsoftware.pl',
    description='Geolocation is a simple and clever application which uses google maps api. '
                'This application allows you to easily and quickly get information about given localisation. '
                'Application returns such information as: country, city, route/street, street number, lat and lng.',
    long_description=readme,
    keywords=['Google Maps Api', 'Google lat', 'Google lng', 'Google Maps'],
    install_requires=['setuptools', 'requests'],
)
