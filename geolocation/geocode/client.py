# -*- coding: utf-8 -*-

import re
from ..client import ApiClient


class GeocodeApiClient(ApiClient):
    """
    Client Class for Geocode Google Maps Api.
    Field query_parameters has keys:
        - address
        - latlng
    Documentation: https://developers.google.com/maps/documentation/geocoding/
    """
    API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
    query_parameters = {}

    def __repr__(self):
        return '<GeocodeApiClient: %s>' % self.api_key

    def prepare_latlng_parameter(self, latitude, longitude):
        """Method prepares correct latitude and longitude value."""
        latlng = "%s,%s" % (latitude, longitude)
        return re.sub('\s+', ' ', latlng).strip()

    def set_query_parameters(self, address=None, latitude=None, longitude=None):
        """Method sets values for query_parameters."""
        if address:
            self.query_parameters['address'] = address
        if latitude and longitude:
            self.query_parameters['latlng'] = self.prepare_latlng_parameter(latitude, longitude)

    def get_data(self, address=None, latitude=None, longitude=None):
        """Method returns json data fetched by calls from API_URL."""
        self.set_query_parameters(
            address=address,
            latitude=latitude,
            longitude=longitude
        )
        return self.send_data(self.API_URL, self.query_parameters)
