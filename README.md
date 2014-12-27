What is Geolocation?
=====================
![Alt text](https://travis-ci.org/slawek87/geolocation-python.svg?branch=master)&nbsp;&nbsp;&nbsp;[![PyPI version](https://badge.fury.io/py/geolocation-python.svg)](https://pypi.python.org/pypi/geolocation-python/0.1.3)&nbsp;&nbsp;&nbsp;
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/slawek87/geolocation-python?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Geolocation is a simple and clever application which uses google maps api.
This application allows you to easily and quickly get information about given location.
Application returns such information as: 

* country, 
* country short form,
* city, 
* route/street, 
* street number,
* postal code,
* formatted address,
* administrative areas,
* lat, 
* lng.

Python2 or Python3?
-------------------
Both!. Currently it supports python 2.7, 3.3 and 3.4.

What do You need?
-----------------
To use this application you need to have Google API key.
    [Google Maps Documentation](https://developers.google.com/maps/documentation/geocoding/) -- Geocoding

1. Open [APIs console](https://code.google.com/apis/console).

  ![Alt text](https://github.com/slawek87/geolocation-python/blob/master/docs/images/geocode-1.png?raw=true "APIs console")

2. Turn On Geocode API.

  ![Alt text](https://github.com/slawek87/geolocation-python/blob/master/docs/images/geocode-2.png?raw=true "Geocode Api")

3. Get your API Key.

  ![Alt text](https://github.com/slawek87/geolocation-python/blob/master/docs/images/geocode-3.png?raw=true "API KEY")


How to install it?
-------------------
    pip install geolocation-python


How to use it?
-----------------------
```python
# -*- coding: utf-8 -*-

from geolocation.google_maps import GoogleMaps

address = "New York City Wall Street 12"

google_maps = GoogleMaps(api_key='your_google_maps_key') 

location = google_maps.search(location=address) # sends search to Google Maps.

print(location.all()) # returns all locations.

my_location = location.first() # returns only first location.

print(my_location.city)
print(my_location.route)
print(my_location.street_number)
print(my_location.postal_code)

for administrative_area in my_location.administrative_area:
    print("{}: {}".format(administrative_area.area_type, administrative_area.name))

print(my_location.country)
print(my_location.country_shortcut)

print(my_location.formatted_address)

print(my_location.lat)
print(my_location.lng)

# reverse geocode

lat = 40.7060008
lng = -74.0088189

my_location = google_maps.search(lat=lat, lng=lng).first()

```
<br/>
![Alt text](https://github.com/iknowledge-io/team/blob/master/images/iknowledge.png)
<br/>    
More examples you should find [here](https://github.com/slawek87/geolocation-python/tree/master/examples).
