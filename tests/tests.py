#!/usr/bin/env python
# encoding: utf-8
from decimal import Decimal

import unittest
from geolocation.distance_matrix.client import DistanceMatrixApiClient
from geolocation.main import GoogleMaps


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

        self.assertAlmostEqual(40.7008854, my_location.lat, delta=0.1)

    def test_lng(self):
        address = "New York City Wall Street 19"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertAlmostEqual(-73.986969, my_location.lng, delta=0.1)

    def test_formatted_address(self):
        address = "New York City 70 Pine Street"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual('70 Pine St, New York, NY 10270, USA',
                         my_location.formatted_address)

    def test_administrative_area_level_1(self):
        address = "New York City Wall Street 125"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual(
            'New York',
            my_location.administrative_area[0].name.decode('utf-8'))

        self.assertEqual(
            'NY',
            my_location.administrative_area[0].short_name.decode('utf-8'))

    def test_administrative_area_level_2(self):
        address = "New York City Wall Street 126"

        location = self.google_maps.search(address)

        my_location = location.first()

        self.assertEqual(
            'New York County',
            my_location.administrative_area[1].name.decode('utf-8'))

        self.assertEqual(
            'New York County',
            my_location.administrative_area[1].short_name.decode('utf-8'))

    def test_coding(self):
        address = "São Paulo"

        my_location = self.google_maps.search(address).first()

        self.assertEqual(u"São Paulo", my_location.city.decode('utf-8'))

    def test_latlng(self):
        lat = 37.4229210
        lng = -122.0852112

        my_location = self.google_maps.search(lat=lat, lng=lng).first()

        self.assertEqual('New York', my_location.city.decode('utf-8'))

    def test_administrative_area_resets(self):
        address = "São Paulo"
        sao_paulo = self.google_maps.search(address).first()

        address = "Houston, TX"
        houston = self.google_maps.search(address).first()

        self.assertNotEqual(sao_paulo, houston)


class DistanceMatrixTest(unittest.TestCase):
    def setUp(self):
        self.google_maps = GoogleMaps(api_key=TEST_API_KEY)
        self.duration_regex = r'([0-9]*)d ([0-9]*)h ([0-9]*)m ([0-9]*)s'
        self.delta_km = 25
        self.delta_m = 25000
        self.delta_miles = 25

    def test_distance_matrix(self):
        origins = ['rybnik', 'oslo']
        destinations = ['zagrzeb']

        items = self.google_maps.distance(origins, destinations).all()

        for item in items:
            if item.origin == 'Rybnik, Poland':
                self.assertEqual(item.destination, 'Zagreb, Croatia')
                self.assertAlmostEqual(Decimal(709), item.distance.kilometers, delta=self.delta_km)
                self.assertAlmostEqual(Decimal(713000), item.distance.meters, delta=self.delta_m)
                self.assertAlmostEqual(Decimal(443.0368), item.distance.miles, delta=self.delta_miles)
                self.assertRegexpMatches(str(item.duration), self.duration_regex)

            if item.origin == 'Oslo, Norway':
                self.assertEqual(item.destination, 'Zagreb, Croatia')
                self.assertAlmostEqual(Decimal(2063), item.distance.kilometers, delta=self.delta_km)
                self.assertAlmostEqual(Decimal(2063000), item.distance.meters, delta=self.delta_m)
                self.assertAlmostEqual(Decimal(1281.8863), item.distance.miles, delta=self.delta_miles)
                self.assertRegexpMatches(str(item.duration), self.duration_regex)

    def test_distance_matrix_bicycling(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_BICYCLING).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertAlmostEqual(Decimal(1596), item.distance.kilometers, delta=self.delta_km)
        self.assertAlmostEqual(Decimal(1596000), item.distance.meters, delta=self.delta_m)
        self.assertAlmostEqual(Decimal(991.7065), item.distance.miles, delta=self.delta_miles)
        self.assertRegexpMatches(str(item.duration), self.duration_regex)

    def test_distance_matrix_walking(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, DistanceMatrixApiClient.MODE_WALKING).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertAlmostEqual(Decimal(1380), item.distance.kilometers, delta=self.delta_km)
        self.assertAlmostEqual(Decimal(1380000), item.distance.meters, delta=self.delta_m)
        self.assertAlmostEqual(Decimal(857.4906), item.distance.miles, delta=self.delta_miles)
        self.assertRegexpMatches(str(item.duration), self.duration_regex)

    def test_distance_matrix_avoid_tolls(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, avoid=DistanceMatrixApiClient.AVOID_TOLLS).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertAlmostEqual(Decimal(1542), item.distance.kilometers, delta=self.delta_km)
        self.assertAlmostEqual(Decimal(1542000), item.distance.meters, delta=self.delta_m)
        self.assertAlmostEqual(Decimal(958.1525), item.distance.miles, delta=self.delta_miles)
        self.assertRegexpMatches(str(item.duration), self.duration_regex)

    def test_distance_matrix_avoid_highways(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, avoid=DistanceMatrixApiClient.AVOID_HIGHWAYS).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertAlmostEqual(Decimal(1542), item.distance.kilometers, delta=self.delta_km)
        self.assertAlmostEqual(Decimal(1542000), item.distance.meters, delta=self.delta_m)
        self.assertAlmostEqual(Decimal(958.1525), item.distance.miles, delta=self.delta_miles)
        self.assertRegexpMatches(str(item.duration), self.duration_regex)

    def test_distance_matrix_avoid_ferries(self):
        origins = ['rybnik']
        destinations = ['oslo']

        item = self.google_maps.distance(origins, destinations, avoid=DistanceMatrixApiClient.AVOID_FERRIES).first()

        self.assertEqual(item.origin, 'Rybnik, Poland')
        self.assertEqual(item.destination, 'Oslo, Norway')
        self.assertAlmostEqual(Decimal(1851), item.distance.kilometers, delta=self.delta_km)
        self.assertAlmostEqual(Decimal(1851000), item.distance.meters, delta=self.delta_m)
        self.assertAlmostEqual(Decimal(1150.1559), item.distance.miles, delta=self.delta_miles)
        self.assertRegexpMatches(str(item.duration), self.duration_regex)


if __name__ == '__main__':
    unittest.main()
