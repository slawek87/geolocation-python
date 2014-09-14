# -*- coding: utf-8 -*-
import json
import re
import urllib2


class GeocodeApi(object):
    STATUS_OK = 'OK'

    _json_api_address = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    _location = None

    def __init__(self, api_key):
        self._api_key = "&key=%s" % api_key

    def __repr__(self):
        return '<Geocode: %s>' % self._location

    def query(self, location):
        """Main method should returns json results."""
        self.set_location(location)

        request = self._prepare_request(location)

        return self._get_json_data(request)

    def set_location(self, location):
        """Method sets location variable."""
        self._location = location

    def _prepare_request(self, query_):
        """Method prepares query to request for google api."""
        prepare = re.sub('\s+', ' ', query_).strip()
        prepare = ',+'.join(prepare.split())

        prepare = "%s%s%s" % (self._json_api_address, prepare, self._api_key)

        return prepare

    def _get_json_data(self, request):
        """Method sends request to google geocode api and returns json data."""
        json_data = urllib2.urlopen(request).read()

        json_results = json.loads(json_data)

        if json_results['status'] == self.STATUS_OK:
            return json_results['results']
        else:
            return None