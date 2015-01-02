# -*- coding: utf-8 -*-
from geolocation.parser import Parser


class DistanceMatrixParser(Parser):
    def get_origin(self):
        """Method returns origin address."""
        return self.json_data.get('origin_addresses')

    def get_destination(self):
        """Method returns destination address."""
        return self.json_data.get('destination_addresses')

    def get_rows(self):
        """Method returns all rows."""
        return self.json_data.get('rows')

    def get_duration(self):
        """Method returns durations in seconds for current element."""
        return self.json_data.get('duration').get('value')

    def get_distance(self):
        """Method returns distance in meters for current element."""
        return self.json_data.get('distance').get('text')