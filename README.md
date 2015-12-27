What is Geolocation 0.2.2?
=====================
![Alt text](https://travis-ci.org/slawek87/geolocation-python.svg?branch=master)&nbsp;&nbsp;&nbsp;[![PyPI version](https://badge.fury.io/py/geolocation-python.svg)](https://pypi.python.org/pypi/geolocation-python/0.2.0)&nbsp;&nbsp;&nbsp;
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/slawek87/geolocation-python?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Geolocation is a simple and clever application which uses google maps api.

1. Geocode Module allows you to easily and quickly get information about given location.

Geocode Module returns such information as: 
* country, 
* country short form,
* city, 
* route/street, 
* street number,
* postal code,
* formatted address,
* administrative areas,
* lat,
* lng


2. Distance Module allows you to get information about travel distance and time for a matrix of origins and destinations.

Distance Module returns such information as:
* origin address
* destination address
* duration
* distance
    - kilometers
    - meters
    - miles

Python2 or Python3?
-------------------
Both!. Currently it supports python 2.7, 3.3 and 3.4.

What do You need?
-----------------
To use this application you need to have Google API key.
    [Google Maps Documentation](https://developers.google.com/maps/documentation/geocoding/) -- Geocoding

1. Open [APIs console](https://code.google.com/apis/console).

  ![Alt text](https://github.com/iknowledge-io/geolocation-python/blob/geolocation-0.2.0/docs/images/geocode-1.png?raw=true "APIs console")

2. Turn On Geocode API.

  ![Alt text](https://github.com/iknowledge-io/geolocation-python/blob/geolocation-0.2.0/docs/images/geocode-2.png?raw=true "Geocode Api")

3. Turn On Distance Matrix API.

  ![Alt text](https://github.com/iknowledge-io/geolocation-python/blob/geolocation-0.2.0/docs/images/distance-1.png?raw=true "Distance Matrix Api")
  
4. Get your API Key.

  ![Alt text](https://github.com/iknowledge-io/geolocation-python/blob/geolocation-0.2.0/docs/images/geocode-3.png?raw=true "API KEY")


How to install it?
-------------------
    pip install geolocation-python


How to use Geocode Module?
----------------------------

```python
# -*- coding: utf-8 -*-

from geolocation.main import GoogleMaps

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
    print("{}: {} ({})".format(administrative_area.area_type, 
                               administrative_area.name, 
                               administrative_area.short_name))

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

How to use Distance Module?
----------------------------
Mode parameter — specifies the mode of transport to use when calculating directions. 

Valid values are:
* driving (default) indicates standard driving directions using the road network.
* walking requests walking directions via pedestrian paths & sidewalks (where available).
* bicycling requests bicycling directions via bicycle paths & preferred streets (currently only available in the US and some Canadian cities).
* transit requests distance calculation via public transit routes (where available).

Avoid parameter -  Directions may be calculated that adhere to certain restrictions. Restrictions are indicated by use of the avoid parameter, and an argument to that parameter indicating the restriction to avoid.

The following restrictions are supported:
* avoid=tolls
* avoid=highways
* avoid=ferries
    
```python
# -*- coding: utf-8 -*-

from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient

origins = ['rybnik', 'oslo']
destinations = ['zagrzeb']

google_maps = GoogleMaps(api_key='your_google_maps_key')

items = google_maps.distance(origins, destinations).all()  # default mode parameter is DistanceMatrixApiClient.MODE_DRIVING.

for item in items:
    print('origin: %s' % item.origin)
    print('destination: %s' % item.destination)
    print('km: %s' % item.distance.kilometers)
    print('m: %s' % item.distance.meters)
    print('miles: %s' % item.distance.miles)
    print('duration: %s' % item.duration)  # returns string.
    print('duration datetime: %s' % item.duration.datetime)  # returns datetime.
    
    # you can also get items from duration, returns int() values.
    print('duration days: %s' % item.duration.days)
    print('duration hours: %s' % item.duration.hours)
    print('duration minutes: %s' % item.duration.minutes)
    print('duration seconds: %s' % item.duration.seconds)
```

Mode Bicycling:
```python
items = google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_BICYCLING).all()

for item in items:
    print('origin: %s' % item.origin)
    print('destination: %s' % item.destination)
    print('km: %s' % item.distance.kilometers)
    print('m: %s' % item.distance.meters)
    print('miles: %s' % item.distance.miles)
    print('duration: %s' % item.duration)
```

Mode Walking:
```python
items = google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_WALKING).all()

for item in items:
    print('origin: %s' % item.origin)
    print('destination: %s' % item.destination)
    print('km: %s' % item.distance.kilometers)
    print('m: %s' % item.distance.meters)
    print('miles: %s' % item.distance.miles)
    print('duration: %s' % item.duration)
```

Mode Transit:
```python
items = google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_TRANSIT).all()

for item in items:
    print('origin: %s' % item.origin)
    print('destination: %s' % item.destination)
    print('km: %s' % item.distance.kilometers)
    print('m: %s' % item.distance.meters)
    print('miles: %s' % item.distance.miles)
    print('duration: %s' % item.duration)
```

Mode Highway:
```python
items = google_maps.distance(origins, destinations, avoid=DistanceMatrixApiClient.AVOID_HIGHWAYS).all()

for item in items:
    print('origin: %s' % item.origin)
    print('destination: %s' % item.destination)
    print('km: %s' % item.distance.kilometers)
    print('m: %s' % item.distance.meters)
    print('miles: %s' % item.distance.miles)
    print('duration: %s' % item.duration)
```

Avoid Ferries:
```python
items = google_maps.distance(origins, destinations, avoid=DistanceMatrixApiClient.AVOID_FERRIES).all()

for item in items:
    print('origin: %s' % item.origin)
    print('destination: %s' % item.destination)
    print('km: %s' % item.distance.kilometers)
    print('m: %s' % item.distance.meters)
    print('miles: %s' % item.distance.miles)
    print('duration: %s' % item.duration)
```

Avoid Tolls:
```python
items = google_maps.distance(origins, destinations, avoid=DistanceMatrixApiClient.AVOID_TOLLS).all()

for item in items:
    print('origin: %s' % item.origin)
    print('destination: %s' % item.destination)
    print('km: %s' % item.distance.kilometers)
    print('m: %s' % item.distance.meters)
    print('miles: %s' % item.distance.miles)
    print('duration: %s' % item.duration)
```

More examples you should find [here](https://github.com/iknowledge-io/geolocation-python/tree/master/examples).
