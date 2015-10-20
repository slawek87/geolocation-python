# -*- coding: utf-8 -*-


class LocationModel(object):
    def __init__(self, **kwargs):
        self.city = kwargs.get('city')
        self.route = kwargs.get('route')
        self.street_number = kwargs.get('street_number')
        self.country = kwargs.get('country')
        self.country_shortcut = kwargs.get('country_shortcut')
        self.postal_code = kwargs.get('postal_code')
        self.lat = kwargs.get('lat')
        self.lng = kwargs.get('lng')
        self.formatted_address = kwargs.get('formatted_address')
        self._administrative_area = list()

    def __repr__(self):
        return '<LocationModel: %s>' % self.city

    @property
    def administrative_area(self):
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, value_list):
        for value in value_list:
            area = AdministrativeAreaLevelModel(value.get('area_type'), value.get('name'), value.get('short_name'))
            self._administrative_area.append(area)


class AdministrativeAreaLevelModel(object):
    def __init__(self, area_type, name, short_name):
        self.area_type = area_type
        self.name = name
        self.short_name = short_name

    def __repr__(self):
        return '<AdministrativeAreaLevelModel: %s>' % self.name
