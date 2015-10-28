from geolocation.geocode.models import LocationModel
from geolocation.managers import Manager
from geolocation.geocode.parsers import GeocodeParser
from geolocation.geocode.client import GeocodeApiClient


class Geocode(object):
    client = GeocodeApiClient()
    parser = GeocodeParser()
    manager = Manager()

    def __init__(self, api_key):
        self.client.api_key = api_key  # set api key

    def build(self, data):
        """Method should converts json_data to python object."""
        self.manager.clear()  # always clear manager data.
        self.parser.data = data

        def validate(location): return False if not location.city else True

        results = self.parser.get_results()

        for result in results:
            self.parser.data = result

            model = LocationModel()

            model.city = self.parser.parse_city()
            model.route = self.parser.parse_route()
            model.street_number = self.parser.parse_street_number()
            model.postal_code = self.parser.parse_postal_code()

            model.country = self.parser.parse_country()
            model.country_shortcut = self.parser.parse_country_shortcut()

            model.administrative_area = self.parser.parse_administrative_area()

            model.lat = self.parser.parse_lat()
            model.lng = self.parser.parse_lng()

            model.formatted_address = self.parser.parse_formatted_address()

            if validate(model):
                self.manager.data.add(model)

    def search(self, address=None, latitude=None, longitude=None):
        data = self.client.get_data(address=address, latitude=latitude, longitude=longitude)

        if data:
            self.build(data)

        return self.manager
