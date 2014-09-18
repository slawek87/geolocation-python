# -*- coding: utf-8 -*-


class LocationModel(object):
    def __init__(self, city=None, route=None, street_number=None, country=None, country_shortcut=None, lat=None,
                 lng=None, formatted_address=None):
        self.city = city
        self.route = route
        self.street_number = street_number
        self.country = country
        self.country_shortcut = country_shortcut
        self.lat = lat
        self.lng = lng
        self.formatted_address = formatted_address

    def __repr__(self):
        return '<LocationModel: %s>' % self.city