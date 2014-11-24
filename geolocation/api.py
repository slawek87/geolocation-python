# -*- coding: utf-8 -*-
import re
import requests
import logging

from geolocation import const


class BaseApi(object):

    log = logging.Logger('google_api')

    def __init__(self, api_key):
        self.api_key = "&key=%s" % api_key

    def get_api_url(self, query_, api):
        """Method should returns api url for request."""
        api_url = "%s%s%s" % (api, query_, self.api_key)

        return api_url

    @staticmethod
    def get_status_code(status):
        """Method should returns information about status code."""
        return dict(const.STATUS_CODES).get(status)

    def send_request(self, request):
        """Method sends request to google geocode api and returns json data."""
        json_results = requests.get(request).json()

        status = json_results['status']

        if status == const.STATUS_OK:
            return json_results['results']

        self.log.warning(self.get_status_code(status))

    def prepare_query(self, location=None, lat=None, lng=None):
        """Method prepares query to request for google api. This method have to be implemented on all apis."""
        raise Exception(const.NOT_IMPLEMENTED)

    def query(self, location=None, lat=None, lng=None):
        """Main method should always returns json results. This method have to be implemented on all apis.."""
        raise Exception(const.NOT_IMPLEMENTED)


class GeocodeApi(BaseApi):
    geocode_api ='https://maps.googleapis.com/maps/api/geocode/json?'
    geocode_api_address = '%saddress=' % geocode_api
    geocode_latlng = '%slatlng=' % geocode_api

    def __repr__(self):
        return '<GeocodeApi: %s>' % self.api_key

    def location_query(self, location):
        """Method is responsible for prepare query geocode address api query."""
        query_ = re.sub('\s+', ' ', location).strip()
        query_ = ',+'.join(query_.split())

        return self.get_api_url(query_, self.geocode_api_address)

    def latlng_query(self, lat, lng):
        """Method is responsible for prepare query geocode reverse api query."""
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

