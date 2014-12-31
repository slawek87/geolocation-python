class DistanceMatrixModel(object):

    def __init__(self, **kwargs):
        self.origin = kwargs.get('origin')
        self.destination = kwargs.get('destination')
        self.distance = kwargs.get('distance')
        self.duration = kwargs.get('duration')

    def __repr__(self):
        return '<DistanceMatrixModel: %s %s>' % (self.origin, self.destination)