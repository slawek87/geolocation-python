# -*- coding: utf-8 -*-
import unittest
from geolocation.google_maps import GoogleMaps


class GeolocationTest(unittest.TestCase):
    def setUp(self):
        self.google_maps = GoogleMaps(api_key='your_google_api_key')

    def test_query(self):
        address = "New York City Wall Steet 12"

        locations = self.google_maps.query(address)

        self.assertGreater(len(locations.all()), 0)

    def test_city(self):
        address = "New York City Wall Steet 12"

        locations = self.google_maps.query(address)

        my_location = locations.first()

        self.assertEqual('New York', my_location.city[0])

    def test_route(self):
        address = "New York City Wall Steet 12"

        locations = self.google_maps.query(address)

        my_location = locations.first()

        self.assertEqual('Wall Street', my_location.route[0])

    def test_country(self):
        address = "New York City Wall Steet 12"

        locations = self.google_maps.query(address)

        my_location = locations.first()

        self.assertEqual('United States', my_location.country[0])

    def test_lat(self):
        address = "New York City Wall Steet 12"

        locations = self.google_maps.query(address)

        my_location = locations.first()

        self.assertEqual(40.7060008, my_location.lat[0])

    def test_lng(self):
        address = "New York City Wall Steet 12"

        locations = self.google_maps.query(address)

        my_location = locations.first()

        self.assertEqual(-74.0088189, my_location.lng[0])

