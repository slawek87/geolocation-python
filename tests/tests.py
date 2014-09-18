# -*- coding: utf-8 -*-
import unittest
from geolocation.google_maps import GoogleMaps

TEST_API_KEY = 'AIzaSyBm0PtaxCuo7iy1KVAnKrl7h8dtA61DXz8'


class GeolocationTest(unittest.TestCase):
    def setUp(self):
        self.google_maps = GoogleMaps(api_key=TEST_API_KEY)

    def test_query(self):
        address = "New York City Wall Steet 12"

        location = self.google_maps.query(address)

        self.assertGreater(len(location.all()), 0)

    def test_city(self):
        address = "New York City Wall Steet 12"

        location = self.google_maps.query(address)

        my_location = location.first()

        self.assertEqual('New York', my_location.city)

    def test_route(self):
        address = "New York City Wall Steet 12"

        location = self.google_maps.query(address)

        my_location = location.first()

        self.assertEqual('Wall Street', my_location.route)

    def test_country(self):
        address = "New York City Wall Steet 12"

        location = self.google_maps.query(address)

        my_location = location.first()

        self.assertEqual('United States', my_location.country)

    def test_country_shortcut(self):
        address = "New York City Wall Steet 12"

        location = self.google_maps.query(address)

        my_location = location.first()

        self.assertEqual('US', my_location.country_shortcut)

    def test_lat(self):
        address = "New York City Wall Steet 12"

        location = self.google_maps.query(address)

        my_location = location.first()

        self.assertEqual(40.7060008, my_location.lat)

    def test_lng(self):
        address = "New York City Wall Steet 12"

        location = self.google_maps.query(address)

        my_location = location.first()

        self.assertEqual(-74.0088189, my_location.lng)

