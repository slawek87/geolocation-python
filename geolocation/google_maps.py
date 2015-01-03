#!/usr/bin/env python
# encoding: utf-8

from geolocation.distance_matrix.main import DistanceMatrix
from geolocation.geocode.main import Geocode
import logging

from geolocation.distance_matrix import const


class GoogleMaps(object):
    """To find address use: GoogleMaps.search(location=full_address)."""
    log = logging.getLogger('google_maps')

    def __init__(self, api_key):
        self._geocode = Geocode(api_key)
        self._distance_matrix = DistanceMatrix(api_key)

    def search(self, location=None, lat=None, lng=None):
        return self._geocode.search(location, lat, lng)

    def distance(self, origins, destinations, mode=const.MODE_DRIVING, avoid=None):
        return self._distance_matrix.distance(origins, destinations, mode, avoid)