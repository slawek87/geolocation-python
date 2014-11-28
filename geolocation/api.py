# -*- coding: utf-8 -*-
import requests
import logging

from geolocation import const


class BaseApi(object):

    log = logging.getLogger('base_api')

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
