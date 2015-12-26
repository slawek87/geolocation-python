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

        self.assertAlmostEqual(40.7008854, my_location.lat, delta=0.009)

    def test_lng(self):
        address = "New York City Wall Street 19"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertAlmostEqual(-74.0777861, my_location.lng, delta=0.09)

    def test_formatted_address(self):
        address = "70 Pine Street, 70 Pine St, New York, NY 10270, USA"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('70 Pine Street, 70 Pine St, New York, NY 10270, USA',
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
                self.assertEqual(item.distance.kilometers, Decimal(716))
                self.assertEqual(item.distance.meters, 716000)
                self.assertEqual(item.distance.miles, 444.9009)
                self.assertEqual(str(item.duration), '0d 7h 34m 54s')

            if item.origin == 'Oslo, Norway':
                self.assertEqual(item.destination, 'Zagreb, Croatia')
                self.assertEqual(item.distance.kilometers, 2069.0)
                self.assertEqual(item.distance.meters, 2069000.0)
                self.assertEqual(item.distance.miles, 1285.6145)
                self.assertEqual(str(item.duration), '0d 21h 36m 30s')

    def test_distance_matrix_bicycling(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, const.MODE_BICYCLING).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertEqual(item.distance.kilometers, 1595)
        self.assertEqual(item.distance.meters, 1595000)
        self.assertEqual(item.distance.miles, 991.0851)
        self.assertEqual(str(item.duration), '3d 10h 59m 41s')

    def test_distance_matrix_walking(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, const.MODE_WALKING).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertEqual(item.distance.kilometers, 1369)
        self.assertEqual(item.distance.meters, 1369000)
        self.assertEqual(item.distance.miles, 850.6555)
        self.assertEqual(str(item.duration), '10d 12h 38m 34s')

    def test_distance_matrix_avoid_tolls(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, avoid=const.AVOID_TOLLS).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertEqual(item.distance.kilometers, 1542)
        self.assertEqual(item.distance.meters, 1542000)
        self.assertEqual(item.distance.miles, 958.1525)
        self.assertEqual(str(item.duration), '0d 16h 36m 5s')

    def test_distance_matrix_avoid_highways(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, avoid=const.AVOID_HIGHWAYS).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertEqual(item.distance.kilometers, 1532.0)
        self.assertEqual(item.distance.meters, 1532000)
        self.assertEqual(item.distance.miles, 951.9388)
        self.assertEqual(str(item.duration), '1d 1h 33m 53s')

    def test_distance_matrix_avoid_ferries(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, avoid=const.AVOID_FERRIES).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertEqual(item.distance.kilometers, 1851)
        self.assertEqual(item.distance.meters, 1851000)
        self.assertEqual(item.distance.miles, 1150.1559)
        self.assertEqual(str(item.duration), '0d 17h 46m 58s')