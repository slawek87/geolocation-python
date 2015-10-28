# encoding: utf-8

from geolocation.distance_matrix.client import DistanceMatrixApiClient
from geolocation.distance_matrix.models import DistanceMatrixModel
from geolocation.distance_matrix.parser import DistanceMatrixParser
from geolocation.managers import Manager


class DistanceMatrix(object):
    client = DistanceMatrixApiClient()
    parser = DistanceMatrixParser()
    manager = Manager()

    def __init__(self, api_key):
        self.client.api_key = api_key

    def build(self, data):
        """Method should converts json_data to python object."""
        self.manager.clear()  # always clear manager data.

        self.parser.data = data

        origins = self.parser.prase_origin()
        destinations = self.parser.parse_destination()

        rows = self.parser.parse_rows()

        origin_counter = 0

        for origin in origins:
            destination_counter = 0

            for element in rows[origin_counter].get('elements'):
                self.parser.data = element

                model = DistanceMatrixModel()
                model.origin = origin
                model.destination = destinations[destination_counter]
                model.distance = self.parser.parse_distance()
                model.duration = self.parser.parse_duration()

                self.manager.data.add(model)

                destination_counter += 1

            origin_counter += 1

    def distance(self, origins, destinations, mode=None, avoid=None):
        """Method returns distance between origins and destination."""
        data = self.client.get_data(origins, destinations, mode, avoid)
        if data:
            self.build(data)
        return self.manager
