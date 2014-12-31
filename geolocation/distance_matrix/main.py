from geolocation.distance_matrix.api import DistanceMatrixApi
from geolocation.distance_matrix.parser import DistanceMatrixParser


class DistanceMatrix():
    parser = DistanceMatrixParser()

    def __init__(self, api_key):
        self.api = DistanceMatrixApi(api_key)

    def to_python(self, json_data):
        """Method should converts json_data to python object."""

        origins = json_data.get('origin_addresses')
        destinations = json_data.get('destination_addresses')

        rows = json_data.get('rows')

        origin_counter = 0

        for origin in origins:
            destination_counter = 0

            for element in rows[origin_counter].get('elements'):
                self.parser.json_data = element
                print destinations[destination_counter], origin, self.parser.get_duration(), self.parser.get_distance()

                destination_counter += 1

            origin_counter += 1

    def search(self, origins, destinations):
        json_data = self.api.query(origins, destinations)

        if json_data:
            self.to_python(json_data)


if __name__ == "__main__":
    distance_matrix = DistanceMatrix('AIzaSyDNvdrZ_HEtfsuPYHV9UvZGc41BSFBolOM')
    distance_matrix.search(['rybnik', 'oslo'], ['zagrzeb', 'oslo'])