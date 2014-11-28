#!/usr/bin/env python
# encoding: utf-8
from geolocation.geocode.main import Geocode
import logging


class GoogleMaps(object):
    """To find address use: GoogleMaps.search(location=full_address)."""
    log = logging.getLogger('google_maps')

    def __init__(self, api_key):
        self.geocode = Geocode(api_key)

    def search(self, location=None, lat=None, lng=None):
        return self.geocode.search(location, lat, lng)

    def query(self, location):
        """Main method should returns GoogleMaps instance."""

        self.log.warning(
            'This method is deprecated. You should call search() method.')

        return self.search(location)
