import re
from geolocation.api import BaseApi


class GeocodeApi(BaseApi):
    geocode_api ='https://maps.googleapis.com/maps/api/geocode/json?'
    geocode_api_address = '%saddress=' % geocode_api
    geocode_latlng = '%slatlng=' % geocode_api

    def __repr__(self):
        return '<GeocodeApi: %s>' % self.api_key

    def location_query(self, location):
        """Method is responsible for prepare query geocode address api query."""
        query_ = re.sub('\s+', ' ', location).strip()
        query_ = ',+'.join(query_.split())

        return self.get_api_url(query_, self.geocode_api_address)

    def latlng_query(self, lat, lng):
        """Method is responsible for prepare query geocode reverse api query."""
        latlng = "%s,%s" % (lat, lng)
        query_ = re.sub('\s+', ' ', latlng).strip()

        return self.get_api_url(query_, self.geocode_latlng)

    def prepare_query(self, location=None, lat=None, lng=None):
        query_ = None

        if location:
            query_ = self.location_query(location)

        if lat and lng:
            query_ = self.latlng_query(lat, lng)

        return query_

    def query(self, location=None, lat=None, lng=None):
        request = self.prepare_query(location=location, lat=lat, lng=lng)

        return self.send_request(request)
