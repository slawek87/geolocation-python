# -*- coding: utf-8 -*-
from geolocation.parsers import Parser


class GeocodeParser(Parser):
    def search_address_components(self, type_, shortcut=False):
        """Method searches address components in google maps json data."""
        data = None

        for address_component in self.data.get('address_components'):
            types = address_component.get('types')

            if type_ in types:
                if shortcut:
                    data = address_component.get('short_name').encode('utf-8')
                else:
                    data = address_component.get('long_name').encode('utf-8')

        return data

    def parse_geometry_location(self, location_type):
        """Method searches geometry location in google maps json data"""
        if not self.data:
            return None

        geometry_location = self.data['geometry']['location']

        return geometry_location[location_type]

    def parse_formatted_address(self):
        """Method should returns full address of current location."""
        if not self.data:
            return None

        return self.data['formatted_address']

    def parse_street_number(self):
        """Method should returns street number of current location."""
        return self.search_address_components('street_number')

    def parse_route(self):
        """Method should returns route long name of current location."""
        return self.search_address_components('route')

    def parse_postal_code(self):
        """Method should returns postal code of current location."""
        return self.search_address_components('postal_code')

    def parse_city(self):
        """Method should returns city long name of current location."""
        return self.search_address_components('locality')

    def parse_country(self):
        """Method should returns country long name from current location."""
        return self.search_address_components('country')

    def parse_country_shortcut(self):
        """Method should returns country short name from current location."""
        return self.search_address_components('country', True)

    def parse_lat(self):
        """Method should returns lat property of current location."""
        return self.parse_geometry_location('lat')

    def parse_lng(self):
        """Method should returns lng property of current location."""
        return self.parse_geometry_location('lng')

    def parse_administrative_area(self):
        """Method should returns all administrative areas of current location."""
        data = list()

        administrative_areas = [
            'administrative_area_level_1', 'administrative_area_level_2', 'administrative_area_level_3'
        ]

        for area_type in administrative_areas:
            name = self.search_address_components(area_type)
            short_name = self.search_address_components(area_type, True)

            if name:
                data.append(dict(name=name, short_name=short_name, area_type=area_type))

        return data

    def get_results(self):
        """Method return results."""
        return self.data.get('results')
