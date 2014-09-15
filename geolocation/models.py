# -*- coding: utf-8 -*-


class LocationModel(object):
    city = None
    route = None
    street_number = None
    country = None
    lat = None
    lng = None
    formatted_address = None

    def __repr__(self):
        return '<LocationModel: %s>' % self.city