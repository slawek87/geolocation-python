# encoding: utf-8

from geolocation.distance_matrix.api import DistanceMatrixApi
from geolocation.distance_matrix.models import DistanceMatrixModel
from geolocation.distance_matrix.parser import DistanceMatrixParser
from geolocation.managers import Manager


class DistanceMatrix():
    parser = DistanceMatrixParser()
    manager = Manager()

    def __init__(self, api_key):
        self.api = DistanceMatrixApi(api_key)

    def to_python(self, json_data):
        """Method should converts json_data to python object."""
        self.manager.clear()  # always clear manager data.

        self.parser.json_data = json_data

        origins = self.parser.get_origin()
        destinations = self.parser.get_destination()

        rows = self.parser.get_rows()

        origin_counter = 0

        for origin in origins:
            destination_counter = 0

            for element in rows[origin_counter].get('elements'):
                self.parser.json_data = element

                model = DistanceMatrixModel()
                model.origin = origin
                model.destination = destinations[destination_counter]
                model.distance = self.parser.get_distance()
                model.duration = self.parser.get_duration()

                self.manager.data.add(model)

                destination_counter += 1

            origin_counter += 1

    def distance(self, origins, destinations, mode, avoid=None):
        """Method returns distance between origins and destination.

            mode — specifies the mode of transport to use when calculating directions. Valid values are:
                * driving (default) indicates standard driving directions using the road network.
                * walking requests walking directions via pedestrian paths & sidewalks (where available).
                * bicycling requests bicycling directions via bicycle paths & preferred streets
                (currently only available in the US and some Canadian cities).

            Directions may be calculated that adhere to certain restrictions. Restrictions are indicated by use
            of the avoid parameter, and an argument to that parameter indicating the restriction to avoid.
            The following estrictions are supported:
                * avoid=tolls
                * avoid=highways
                * avoid=ferries"""
        json_data = self.api.query(origins, destinations, mode, avoid)

        if json_data:
            self.to_python(json_data)

        return self.manager