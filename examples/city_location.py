# -*- coding: utf-8 -*-
from geolocation.google_maps import GoogleMaps

if __name__ == "__main__":
    address = "New York City"

    google_maps = GoogleMaps(api_key='your_google_maps_key')

    location = google_maps.query(location=address)

    print location.all()

    my_location = location.first()

    print my_location.city
    print my_location.route
    print my_location.street_number
    print my_location.country
    print my_location.country_shortcut
    print my_location.lat
    print my_location.lng
