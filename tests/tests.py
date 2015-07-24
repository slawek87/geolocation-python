#!/usr/bin/env python
# encoding: utf-8

from decimal import Decimal

import unittest
from geolocation.google_maps import GoogleMaps
from geolocation.distance_matrix import const


TEST_API_KEY = 'AIzaSyDNvdrZ_HEtfsuPYHV9UvZGc41BSFBolOM'


class GeolocationTest(unittest.TestCase):
    def setUp(self):
        self.google_maps = GoogleMaps(api_key=TEST_API_KEY)

    def test_query(self):
        address = "New York City Wall Street 15"

        location = self.google_maps.search(address)

        self.assertIsNotNone(location.all())

    def test_city(self):
        address = "New York City Wall Street 14"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('New York', my_location.city.decode('utf-8'))

    def test_route(self):
        address = "New York City Wall Street 12"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('Wall Street', my_location.route.decode('utf-8'))

    def test_country(self):
        address = "New York City Wall Street 110"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('United States', my_location.country.decode('utf-8'))

    def test_country_shortcut(self):
        address = "New York City Wall Street 2"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('US', my_location.country_shortcut.decode('utf-8'))

    def test_lat(self):
        address = "New York City Wall Street 1"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual(40.7060081, my_location.lat)

    def test_lng(self):
        address = "New York City Wall Street 19"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual(-74.0134436, my_location.lng)

    def test_formatted_address(self):
        address = "New York City Wall Street 124"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('Charging Bull, Broadway, New York, NY 10004, USA',
                         my_location.formatted_address)

    def test_administrative_area_level_1(self):
        address = "New York City Wall Street 125"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual(
            'New York',
            my_location.administrative_area[0].name.decode('utf-8'))

    def test_administrative_area_level_2(self):
        address = "New York City Wall Street 126"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual(
            'New York County',
            my_location.administrative_area[1].name.decode('utf-8'))

    def test_coding(self):
        address = "São Paulo"

        my_location = self.google_maps.search(address).first()

        self.assertEqual(u"São Paulo", my_location.city.decode('utf-8'))

    def test_latlng(self):
        lat = 37.4229210
        lng = -122.0852112

        my_location = self.google_maps.search(lat=lat, lng=lng).first()

        self.assertEqual('Mountain View', my_location.city.decode('utf-8'))

    def test_administrative_area_resets(self):
        address = "São Paulo"

        my_location = self.google_maps.search(address).first()

        self.assertEqual(len(my_location.administrative_area), 2)

        address = "Rio de Janeiro"

        my_location = self.google_maps.search(address).first()

        self.assertEqual(len(my_location.administrative_area), 2)


class DistanceMatrixTest(unittest.TestCase):
    def setUp(self):
        self.google_maps = GoogleMaps(api_key=TEST_API_KEY)

    def test_distance_matrix(self):
        origins = ['rybnik', 'oslo']
        destinations = ['zagrzeb']

        items = self.google_maps.distance(origins, destinations).all()

        for item in items:
            if item.origin == 'Rybnik, Poland':
                self.assertEqual(item.destination, 'Zagreb, Croatia')
                self.assertEqual(item.distance.kilometers, Decimal(713))
                self.assertEqual(item.distance.meters, 713000)
                self.assertEqual(item.distance.miles, 443.0368)
                self.assertEqual(str(item.duration), '0d 7h 7m 47s')

            if item.origin == 'Oslo, Norway':
                self.assertEqual(item.destination, 'Zagreb, Croatia')
                self.assertEqual(item.distance.kilometers, 2063)
                self.assertEqual(item.distance.meters, 2063000)
                self.assertEqual(item.distance.miles, 1281.8863)
                self.assertEqual(str(item.duration), '0d 21h 18m 29s')

    def test_distance_matrix_bicycling(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, const.MODE_BICYCLING).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertEqual(item.distance.kilometers, 1596)
        self.assertEqual(item.distance.meters, 1596000)
        self.assertEqual(item.distance.miles, 991.7065)
        self.assertEqual(str(item.duration), '3d 11h 7m 25s')

    def test_distance_matrix_walking(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, const.MODE_WALKING).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertEqual(item.distance.kilometers, 1380)
        self.assertEqual(item.distance.meters, 1380000)
        self.assertEqual(item.distance.miles, 857.4906)
        self.assertEqual(str(item.duration), '10d 9h 32m 16s')

    def test_distance_matrix_avoid_tolls(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, avoid=const.AVOID_TOLLS).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertEqual(item.distance.kilometers, 1542)
        self.assertEqual(item.distance.meters, 1542000)
        self.assertEqual(item.distance.miles, 958.1525)
        self.assertEqual(str(item.duration), '0d 16h 30m 40s')

    def test_distance_matrix_avoid_highways(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, avoid=const.AVOID_HIGHWAYS).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertEqual(item.distance.kilometers, 1491)
        self.assertEqual(item.distance.meters, 1491000)
        self.assertEqual(item.distance.miles, 926.4627)
        self.assertEqual(str(item.duration), '1d 1h 36m 6s')

    def test_distance_matrix_avoid_ferries(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, avoid=const.AVOID_FERRIES).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertEqual(item.distance.kilometers, 1851)
        self.assertEqual(item.distance.meters, 1851000)
        self.assertEqual(item.distance.miles, 1150.1559)
        self.assertEqual(str(item.duration), '0d 17h 35m 44s')


if __name__ == '__main__':
    unittest.main()
