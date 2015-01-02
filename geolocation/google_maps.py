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
        self.geocode = Geocode(api_key)
        self.distance_matrix = DistanceMatrix(api_key)

    def search(self, location=None, lat=None, lng=None):
        return self.geocode.search(location, lat, lng)

    def distance(self, origins, destinations, mode=const.MODE_DRIVING, avoid=None):
        return self.distance_matrix.distance(origins, destinations, mode, avoid)


# if __name__ == "__main__":
#     gmaps = GoogleMaps('AIzaSyDNvdrZ_HEtfsuPYHV9UvZGc41BSFBolOM')
#
#     for item in gmaps.distance(['rybnik', 'oslo'], ['zagrzeb', 'oslo'], const.MODE_BICYCLING, const.AVOID_HIGHWAYS):
#         print "duration: %s" % item.duration
#         print "km: %s" % item.distance.kilometers
#         print "m: %s" % item.distance.meters
#         print "miles: %s" % item.distance.miles