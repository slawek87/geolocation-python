# encoding: utf-8

import datetime
import re

from geolocation.distance_matrix import const


class DistanceMatrixModel(object):

    def __init__(self, **kwargs):
        self.origin = kwargs.get('origin')
        self.destination = kwargs.get('destination')
        self._distance = kwargs.get('distance', 0)
        self._duration = kwargs.get('duration')

    def __repr__(self):
        return '<DistanceMatrixModel: %s %s>' % (self.origin, self.destination)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        duration = datetime.timedelta(seconds=value)

        model = Duration()
        model.datetime = duration

        str_duration = str(duration)

        if duration.days:
            pattern = r'(?P<days>\d+)\s(days|day),\s(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+)$'
            model.days = int(re.match(pattern, str_duration).group('days'))
        else:
            pattern = r'(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+)$'

        model.hours = int(re.match(pattern, str_duration).group('hours'))
        model.minutes = int(re.match(pattern, str_duration).group('minutes'))
        model.seconds = int(re.match(pattern, str_duration).group('seconds'))

        self._duration = model

    @property
    def distance(self):
        return self._distance


    @distance.setter
    def distance(self, value):
        model = Distance()

        if value:
            pattern = r'(?P<value>[\d,]+)\s(?P<unit>km|m)$'

            unit = re.match(pattern, value).group('unit')
            value = re.match(pattern, value).group('value').replace(',', '').replace('.', ',')

            if unit == const.UNIT_KM:
                model.kilometers = float(value)
                model.meters = float(value)*const.ONE_KILOMETER
            else:
                model.kilometers = float(value)/const.ONE_KILOMETER
                model.meters = float(value)

        self._distance = model


class Duration(object):
    def __init__(self, **kwargs):
        self.days = int(kwargs.get('days', 0))
        self.hours = int(kwargs.get('hours', 0))
        self.minutes = int(kwargs.get('minutes', 0))
        self.seconds = int(kwargs.get('seconds', 0))
        self.datetime = (kwargs.get('datetime'), None)

    def __str__(self):
        return "%sd %sh %sm %ss" % (self.days, self.hours, self.minutes, self.seconds)


class Distance(object):
    def __init__(self, **kwargs):
        self._meters = round(float(kwargs.get('meters', 0)), 3)
        self._kilometers = round(float(kwargs.get('kilometers', 0)), 3)

    def __str__(self):
        return "%s km" % round(self.kilometers, 3)

    @property
    def meters(self):
        return self._meters

    @meters.setter
    def meters(self, value):
        self._meters = round(float(value), 3)

    @property
    def kilometers(self):
        return self._kilometers

    @kilometers.setter
    def kilometers(self, value):
        self._kilometers = round(float(value), 3)

    @property
    def miles(self):
        return round(float(self.kilometers*const.ONE_MILE), 4)
