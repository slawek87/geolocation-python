from geolocation.geocode.models import LocationModel
from geolocation.managers import Manager
from geolocation.geocode.parsers import GeocodeParser
from geolocation.geocode.api import GeocodeApi


class Geocode():
    parser = GeocodeParser()
    manager = Manager()

    def __init__(self, api_key):
        self.api = GeocodeApi(api_key)

    @staticmethod
    def validate(location):
        """Method should always returns false when location doesn't have city value."""
        if not location.city:
            return False

        return True

    def to_python(self, json_data):
        """Method should converts json_data to python object."""
        self.manager.clear()  # always clear manager data.
        self.parser.json_data = json_data

        results = self.parser.get_results()

        for result in results:
            self.parser.json_data = result

            model = LocationModel()

            model.city = self.parser.get_city()
            model.route = self.parser.get_route()
            model.street_number = self.parser.get_street_number()
            model.postal_code = self.parser.get_postal_code()

            model.country = self.parser.get_country()
            model.country_shortcut = self.parser.get_country_shortcut()

            model.administrative_area = self.parser.get_administrative_area()

            model.lat = self.parser.get_lat()
            model.lng = self.parser.get_lng()

            model.formatted_address = self.parser.get_formatted_address()

            if self.validate(model):
                self.manager.data.add(model)

    def search(self, location=None, lat=None, lng=None):
        json_data = self.api.query(location=location, lat=lat, lng=lng)

        if json_data:
            self.to_python(json_data)

        return self.manager