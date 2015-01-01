# -*- coding: utf-8 -*-

import re
import requests
import logging

from geolocation import const


class BaseApi(object):

    log = logging.getLogger('base_api')

    def __init__(self, api_key):
        self.api_key = "&key=%s" % api_key

    @staticmethod
    def to_list(data):
        if not isinstance(data, list):
            data = [data]

        return data

    @staticmethod
    def join_query(string):
        return '+'.join(re.sub('\s+', ' ', string).strip().split())

    def get_api_url(self, query, api):
        """Method should returns api url for request."""
        api_url = "%s%s%s" % (api, query, self.api_key)

        return api_url

    @staticmethod
    def get_status_code(status):
        """Method should returns information about status code."""
        return dict(const.STATUS_CODES).get(status)

    def send_request(self, query):
        """Method sends request to GoogleMaps api and returns respond with json data."""
        respond = requests.get(query).json()

        status = respond.get('status')

        if status == const.STATUS_OK:
            return respond

        self.log.warning(self.get_status_code(status))

        return None
