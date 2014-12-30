class GeocodeManager(object):
    data = set()

    def __init__(self):
        self.clear()

    def __getitem__(self, key):
        return self.list_data[key]

    def __setitem__(self, key, value):
        self.list_data[key] = value

    @property
    def list_data(self):
        return list(self.data)

    def clear(self):
        """Method is clearing data when we call new search() method."""
        self.data = set()

    def all(self):
        """Method should returns location list."""
        return self.list_data

    def first(self):
        if self.data:
            return self.list_data[0]

        return None
