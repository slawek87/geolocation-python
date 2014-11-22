# -*- coding: utf-8 -*-
import re
import requests
import logging


STATUS_OK = 'OK'
STATUS_ZERO_RESULTS = 'ZERO_RESULTS'
STATUS_OVER_QUERY_LIMIT = 'OVER_QUERY_LIMIT'
STATUS_REQUEST_DENIED = 'REQUEST_DENIED'
STATUS_INVALID_REQUEST = 'INVALID_REQUEST'
STATUS_UNKNOWN_ERROR = 'UNKNOWN_ERROR'

STATUS_CODES = (
    (STATUS_OK, 'Successfully parsed.'),
    (STATUS_ZERO_RESULTS, 'Successful parsed but returned no results.'),
    (STATUS_OVER_QUERY_LIMIT, 'Over your quota.'),
    (STATUS_REQUEST_DENIED, 'Request was denied.'),
    (STATUS_INVALID_REQUEST, 'Query is missing.'),
    (STATUS_UNKNOWN_ERROR, 'Request could not be processed due to a server'
                           'error. Try again.'),
)

NOT_IMPLEMENTED = 'Method is not implemented.'


class BaseApi(object):
    STATUS_OK = 'OK'

    def __init__(self, api_key):
        self.api_key = "&key=%s" % api_key

    def get_api_url(self, query_, api):
        """Method should returns api url for request."""
        api_url = "%s%s%s" % (api, query_, self.api_key)

        return api_url

    def prepare_query(self, location=None, latlng=None):
        """Method prepares query to request for google api. This method have to be implemented on all apis."""
        raise Exception(NOT_IMPLEMENTED)

    @staticmethod
    def get_status(status):
        """Method should returns information about status code."""
        return dict(STATUS_CODES).get(status)

    def send_request(self, request):
        """Method sends request to google geocode api and returns json data."""
        json_results = requests.get(request).json()

        status = json_results['status']

        if status == STATUS_OK:
            return json_results['results']

        logging.warning(self.get_status(status))

    def query(self, location=None, lat=None, lng=None):
        """Main method should always returns json results. This is default method for all apis.
        This method is deprecated!"""


class GeocodeApi(BaseApi):
    geocode_api ='https://maps.googleapis.com/maps/api/geocode/json?'
    geocode_api_address = '%saddress=' % geocode_api
    geocode_latlng = '%slatlng=' % geocode_api

    def __repr__(self):
        return '<GeocodeApi: %s>' % self.get_api_url()

    def location_query(self, location):
        """Method is responsible for prepare query for geocode address api."""
        query_ = re.sub('\s+', ' ', location).strip()
        query_ = ',+'.join(query_.split())

        return self.get_api_url(query_, self.geocode_api_address)

    def latlng_query(self, lat, lng):
        """Method is responsible for prepare query for geocode reverse api."""
        latlng = "%s,%s" % (lat, lng)
        query_ = re.sub('\s+', ' ', latlng).strip()

        return self.get_api_url(query_, self.geocode_latlng)

    def prepare_query(self, location=None, lat=None, lng=None):
        query_ = None

        if location:
            query_ = self.location_query(location)

        if lat and lng:
            query_ = self.latlng_query(lat, lng)

        return query_

    def query(self, location=None, lat=None, lng=None):
        request = self.prepare_query(location=location, lat=lat, lng=lng)

        return self.send_request(request)

