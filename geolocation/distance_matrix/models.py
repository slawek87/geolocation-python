import datetime
from decimal import Decimal
import re

ONE_MILE = Decimal(0.62137)
ONE_FEET = Decimal(3.2808)

ONE_KILOMETER = Decimal(1000.00)


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
        model = Duration()

        str_duration = str(self._duration)

        if self._duration.days:
            pattern = r'(?P<days>\d)\sdays,\s(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+)'
            model.days = int(re.match(pattern, str_duration).group('days'))
        else:
            pattern = r'(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+)'

        model.hours = int(re.match(pattern, str_duration).group('hours'))
        model.minutes = int(re.match(pattern, str_duration).group('minutes'))
        model.seconds = int(re.match(pattern, str_duration).group('seconds'))

        return model

    @duration.setter
    def duration(self, value):
        self._duration = datetime.timedelta(seconds=value)

    @property
    def distance(self):
        print self._distance
        kilometers, meters = str(self._distance).split('.')

        model = Distance()
        model.kilometers = int(kilometers)
        model.meters = int(meters)

        return model


    @distance.setter
    def distance(self, value):
        self._distance = float(value)/1000


class Duration(object):
    def __init__(self, **kwargs):
        self.days = int(kwargs.get('days', 0))
        self.hours = int(kwargs.get('hours', 0))
        self.minutes = int(kwargs.get('minutes', 0))
        self.seconds = int(kwargs.get('seconds', 0))


class Distance(object):
    def __init__(self, **kwargs):
        self.meters = int(kwargs.get('meters', 0))
        self.kilometers = int(kwargs.get('kilometers', 0))

    @property
    def miles(self):
        return round((self.kilometers + (self.meters/ONE_KILOMETER))*ONE_MILE, 4)
