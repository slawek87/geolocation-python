#!/usr/bin/env python
# encoding: utf-8

import unittest
from geolocation.google_maps import GoogleMaps


TEST_API_KEY = 'AIzaSyDNvdrZ_HEtfsuPYHV9UvZGc41BSFBolOM',


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

