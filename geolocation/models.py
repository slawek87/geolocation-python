class LocationModel(object):
    _city = None
    _route = None
    _street_number = None
    _country = None
    _lat = None
    _lng = None
    _formatted_address = None

    def __repr__(self):
        return '<LocationModel: %s>' % self.city

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, value):
        self._route = value

    @property
    def street_number(self):
        return self._street_number

    @street_number.setter
    def street_number(self, value):
        self._street_number = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value

    @property
    def lng(self):
        return self._lng

    @lng.setter
    def lng(self, value):
        self._lng = value

    @property
    def formatted_address(self):
        return self._formatted_address

    @formatted_address.setter
    def formatted_address(self, value):
        self._formatted_address = value