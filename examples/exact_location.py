# -*- coding: utf-8 -*-
from geolocation.google_maps import GoogleMaps

if __name__ == "__main__":
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
