# -*- coding: utf-8 -*-
from distutils.core import setup

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE', 'r') as f:
    license_ = f.read()

setup(
    name='Geolocation',
    version='0.1.0',
    packages=['geolocation'],
    url='',
    license=license_,
    author=u'Sławomir Kabik',
    author_email='slawek@redsoftware.pl',
    description='Geolocation is a simple and clever application which uses google maps api.'
                'This application allows you to easily and quickly get information about given localisation.'
                'Application returns such information as: country, city, country, route/street, lnt ang lng.',
    long_description=readme,
)
