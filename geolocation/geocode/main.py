from geolocation.geocode.models import LocationModel
from geolocation.managers import GeocodeManager
from geolocation.geocode.parsers import GeocodeParser
from geolocation.geocode.api import GeocodeApi


class Geocode(GeocodeManager):
    parser = GeocodeParser()

    def __init__(self, api_key):
        super(Geocode, self).__init__()
        self.api = GeocodeApi(api_key)

    def __repr__(self):
        return '<Geocode %s >' % self.all()

    @staticmethod
    def validate(location):
        """Method should always returns false when location doesn't have city value."""
        if not location.city:
            return False

        return True

    def to_python(self, json_data):
        """Method should converts json_data to python object."""
        for item in json_data:
            self.parser.json_data = item

            location = LocationModel()

            location.city = self.parser.get_city()
            location.route = self.parser.get_route()
            location.street_number = self.parser.get_street_number()
            location.postal_code = self.parser.get_postal_code()

            location.country = self.parser.get_country()
            location.country_shortcut = self.parser.get_country_shortcut()

            location.administrative_area = self.parser.get_administrative_area()

            location.lat = self.parser.get_lat()
            location.lng = self.parser.get_lng()

            location.formatted_address = self.parser.get_formatted_address()

            if self.validate(location):
                self.data.add(location)

    def search(self, location=None, lat=None, lng=None):
        json_data = self.api.query(location=location, lat=lat, lng=lng)

        if json_data:
            self.to_python(json_data)

        return self