# -*- coding: utf-8 -*-


class LocationModel(object):
    _administrative_area = list()

    def __init__(self, **kwargs):
        self.city = kwargs.get('city', None)
        self.route = kwargs.get('route', None)
        self.street_number = kwargs.get('street_number', None)
        self.country = kwargs.get('country', None)
        self.country_shortcut = kwargs.get('country_shortcut', None)
        self.postal_code = kwargs.get('postal_code', None)
        self.lat = kwargs.get('lat', None)
        self.lng = kwargs.get('lng', None)
        self.formatted_address = kwargs.get('formatted_address', None)

    def __repr__(self):
        return '<LocationModel: %s>' % self.city

    @property
    def administrative_area(self):
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, value_list):
        for value in value_list:
            area = AdministrativeAreaLevelModel(value['area_type'], value['name'])
            self._administrative_area.append(area)


class AdministrativeAreaLevelModel(object):
    def __init__(self, area_type, name):
        self.area_type = area_type
        self.name = name

    def __repr__(self):
        return '<AdministrativeAreaLevelModel: %s>' % self.name