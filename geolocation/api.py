# -*- coding: utf-8 -*-
import re
import requests


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


class GeocodeApi(object):
    STATUS_OK = 'OK'

    _json_api_address =\
        'https://maps.googleapis.com/maps/api/geocode/json?address='

    location = None

    def __init__(self, api_key):
        self._api_key = "&key=%s" % api_key

    def __repr__(self):
        return '<Geocode: %s>' % self.location

    def query(self, location):
        """Main method should returns json results."""
        self.set_location(location)

        request = self._prepare_request(location)

        return self._get_json_data(request)

    def set_location(self, location):
        """Method sets location variable."""
        self.location = location

    def _prepare_request(self, query_):
        """Method prepares query to request for google api."""
        prepare = re.sub('\s+', ' ', query_).strip()
        prepare = ',+'.join(prepare.split())

        prepare = "%s%s%s" % (self._json_api_address, prepare, self._api_key)

        return prepare

    @staticmethod
    def _get_status_code(status):
        """Method should returns information about status code."""
        return dict(STATUS_CODES)[status]

    def _get_json_data(self, request):
        """Method sends request to google geocode api and returns json data."""
        # with requests lib we don't need a if/else for urlllib py2/py3
        json_results = requests.get(request).json()

        status = json_results['status']

        if status == STATUS_OK:
            return json_results['results']
        else:
            raise self._get_status_code(status)
