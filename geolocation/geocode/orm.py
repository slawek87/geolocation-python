class GeocodeOrm(object):
    def __init__(self, data):
        self.data = data

    def all(self):
        """Method returns location list."""
        return list(self.data)

    def first(self):
        if self.data:
            return list(self.data)[0]

        return None
