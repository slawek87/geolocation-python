from geolocation.google_maps import GoogleMaps

if __name__ == "__main__":
    address = "Rybnik Adama Mickiewicza 18"

    test = google_maps = GoogleMaps.query(address)
    print test.all()

    test = test.first()

    print test.city
    print test.route
    print test.street_number
    print test.country
    print test.lat
    print test.lng
    #print test.map_static
