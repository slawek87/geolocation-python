# -*- coding: utf-8 -*-
import requests
from geolocation.validators import ResponseValidator


class ApiClient(object):
    """
    Client class:
        - sends request to API
        - returns data from API
        - handles exceptions
    All clients should inheritance by this class.
    """
    api_key = None  # api key for google maps.
    validator = ResponseValidator

    def __repr__(self):
        return '<ApiClient: %s>' % self.api_key

    def send_data(self, url, params=None):
        """Method class url api and returns json data."""
        response = requests.get(url, params=params)
        self.validator(response)

        return response.json()