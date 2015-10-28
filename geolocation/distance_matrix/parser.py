# -*- coding: utf-8 -*-

from geolocation.parsers import Parser


class DistanceMatrixParser(Parser):
    def prase_origin(self):
        """Method returns origin address."""
        return self.data.get('origin_addresses')

    def parse_destination(self):
        """Method returns destination address."""
        return self.data.get('destination_addresses')

    def parse_rows(self):
        """Method returns all rows."""
        return self.data.get('rows')

    def parse_duration(self):
        """Method returns durations in seconds for current element."""
        duration = self.data.get('duration')
        value = duration.get('value') if duration else 0
        return value

    def parse_distance(self):
        """Method returns distance in meters for current element."""
        distance = self.data.get('distance')
        value = distance.get('text') if distance else 0
        return value
