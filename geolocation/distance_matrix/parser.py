# -*- coding: utf-8 -*-
from geolocation.parser import Parser


class DistanceMatrixParser(Parser):
    def get_duration(self):
        """Method returns durations in seconds for current element."""
        return self.json_data.get('duration').get('value')

    def get_distance(self):
        """Method returns distance in meters for current element."""
        return self.json_data.get('distance').get('value')