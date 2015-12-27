# -*- coding: utf-8 -*-
from distutils.core import setup

try:
    with open('README.md', 'r') as f:
        readme = f.read()

    with open('LICENSE.txt', 'r') as f:
        license_ = f.read()
except:
    readme = ''
    license_ = ''

setup(
    name='geolocation-python',
    version='0.2.2',
    packages=['geolocation', 'geolocation.distance_matrix', 'geolocation.geocode'],
    url='',
    download_url='https://github.com/slawek87/geolocation-python/',
    license=license_,
    author=u'Sławomir Kabik',
    author_email='slawek@redsoftware.pl',
    description='Geolocation is a simple and clever application which uses google maps api. '
                'This application allows you to easily and quickly get information about given localisation. '
                'Application returns such information as: country, city, route/street, street number, lat and lng,'
                'travel distance and time for a matrix of origins and destinations.',
    long_description=readme,
    keywords=['Python Google Maps Api', 'Google lat', 'Google lng', 'Python Google Maps', 'Google Maps Distance'],
    install_requires=['setuptools', 'requests'],
)
