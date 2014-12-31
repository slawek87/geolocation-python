# -*- coding: utf-8 -*-


class Parser(object):
    _json_data = None

    @property
    def json_data(self):
        return self._json_data

    @json_data.setter
    def json_data(self, value):
        self._json_data = value
