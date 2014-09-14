# -*- coding: utf-8 -*-
from models import LocationModel
from parsers import GeocodeParser
from api import GeocodeApi


class GoogleMaps(object):
    """To find address use: GoogleMaps.query(location=full_address)."""
    _geocode_parser = GeocodeParser()

    _location = None

    _data = set()

    def __init__(self, api_key):
        self._geocode_api = GeocodeApi(api_key)

    def __repr__(self):
        return '<GoogleMaps: %s>' % self._location

    def _to_python(self, json_results):
        """Method should converts json_results to python object."""
        for item in json_results:
            self._geocode_parser.json_data = item

            location = LocationModel()
            location.city = self._geocode_parser.get_city(),
            location.route = self._geocode_parser.get_route(),
            location.street_number = self._geocode_parser.get_street_number(),
            location.country = self._geocode_parser.get_country(),
            location.lat = self._geocode_parser.get_lat(),
            location.lng = self._geocode_parser.get_lng(),
            location.formatted_address = self._geocode_parser.get_formatted_address()

            self._data.add(location)

        return self.all()

    def set_location(self, location):
        """Method sets location variable."""
        self._location = location

    def all(self):
        """Method returns location list."""
        return list(self._data)

    def first(self):
        if self._data:
            return list(self._data)[0]

        return None

    def query(self, location):
        """Main method should returns GoogleMaps instance."""
        self.set_location(location)

        json_results = self._geocode_api.query(location)

        if json_results:
            self._to_python(json_results)

        return self
