#!/usr/bin/env python
# encoding: utf-8

from geolocation.models import LocationModel
from geolocation.parsers import GeocodeParser
from geolocation.api import GeocodeApi
import logging


class GoogleMaps(object):
    """To find address use: GoogleMaps.search(location=full_address)."""
    geocode = GeocodeParser()
    data = set()

    log = logging.Logger('google_maps')

    def __init__(self, api_key):
        self._geocode_api = GeocodeApi(api_key)
        self.clear()

    def __repr__(self):
        return '<GoogleMaps %s >' % self.all()

    def clear(self):
        self.data = set()

    @staticmethod
    def validate(location):
        """Method should always returns false when location doesn't have city value."""
        if not location.city:
            return False

        return True

    def _to_python(self, json_results):
        """Method should converts json_results to python object."""
        for item in json_results:
            self.geocode.json_data = item

            location = LocationModel()

            location.city = self.geocode.get_city()
            location.route = self.geocode.get_route()
            location.street_number = self.geocode.get_street_number()
            location.postal_code = self.geocode.get_postal_code()

            location.country = self.geocode.get_country()
            location.country_shortcut = self.geocode.get_country_shortcut()

            location.administrative_area = self.geocode.get_administrative_area()

            location.lat = self.geocode.get_lat()
            location.lng = self.geocode.get_lng()

            location.formatted_address = self.geocode.get_formatted_address()

            if self.validate(location):
                self.data.add(location)

        return self.all()

    def all(self):
        """Method returns location list."""
        return list(self.data)

    def first(self):
        if self.data:
            return list(self.data)[0]

        return None

    def search(self, location=None, lat=None, lng=None):
        json_results = self._geocode_api.query(location=location, lat=lat, lng=lng)

        if json_results:
            self._to_python(json_results)

        return self

    def query(self, location):
        """Main method should returns GoogleMaps instance."""

        self.log.warning(
            'This method is deprecated. You should call search() method.')

        return self.search(location)
