# -*- coding: utf-8 -*-

import re
from geolocation.api import BaseApi


class GeocodeApi(BaseApi):
    api ='https://maps.googleapis.com/maps/api/geocode/json?'
    address_parameter = '%saddress=' % api
    latlng_parameter = '%slatlng=' % api

    def __repr__(self):
        return '<GeocodeApi: %s>' % self.api_key

    def prepare_location_query(self, location):
        query_ = self.join_query(location)

        return self.get_api_url(query_, self.address_parameter)

    def prepare_latlng_query(self, lat, lng):
        latlng = "%s,%s" % (lat, lng)
        query_ = re.sub('\s+', ' ', latlng).strip()

        return self.get_api_url(query_, self.latlng_parameter)

    def prepare_query(self, location=None, lat=None, lng=None):
        query_ = None

        if location:
            query_ = self.prepare_location_query(location)

        if lat and lng:
            query_ = self.prepare_latlng_query(lat, lng)

        return query_

    def query(self, location=None, lat=None, lng=None):
        query_ = self.prepare_query(location=location, lat=lat, lng=lng)

        return self.send_request(query_)
