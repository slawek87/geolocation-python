What is Geolocation?
=====================
Geolocation is a simple and clever application which uses google maps api.
This application allows you to easily and quickly get information about given localization.
Application returns such information as: 

* country, 
* city, 
* route/street, 
* street number,
* lat, 
* lng.


What do You need?
-----------------
To use this application you need to have Google API key.
    [Google Maps Documentation](https://developers.google.com/maps/documentation/geocoding/) -- Geocoding


How to install it?
-------------------
    pip install geolocation-python


How to use it?
-----------------------
    # -*- coding: utf-8 -*-
    
    from geolocation.google_maps import GoogleMaps
    
    address = "New York City Wall Street 12"

    google_maps = GoogleMaps(api_key='your_google_maps_key')

    location_info = google_maps.query(location=address)

    print location_info.all()

    location_info = location_info.first()

    print location_info.city
    print location_info.route
    print location_info.street_number
    print location_info.country
    print location_info.lat
    print location_info.lng
    
More examples you should find in https://github.com/slawek87/geolocation-python/tree/master/examples