import json
import re
import urllib2

from config import GOOGLE_MAPS_API_KEY


class GeocodeApi(object):
    STATUS_OK = 'OK'

    _api_key = "&key=%s" % GOOGLE_MAPS_API_KEY
    _json_api_address = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    _location = None

    def __repr__(self):
        return '<Geocode: %s>' % self._location

    @classmethod
    def query(cls, location):
        """Main method should returns json results."""
        instance = cls()
        instance.set_location(location)

        request = instance._prepare_request(location)

        return instance._get_json_data(request)

    def set_location(self, location):
        """Method sets location variable."""
        self._location = location

    def _prepare_request(self, query_):
        """Method prepares query for google api request."""
        if not GOOGLE_MAPS_API_KEY:
            raise Exception('GOOGLE_MAPS_API_KEY is empty.')

        prepare = query_.encode('ascii', 'ignore').decode('ascii')
        prepare = re.sub('\s+', ' ', prepare).strip()
        prepare = ',+'.join(prepare.split())

        prepare = "%s%s%s" % (self._json_api_address, prepare, self._api_key)

        return prepare

    def _get_json_data(self, request):
        """Method sends request to google geocode api and returns json data."""
        json_data = urllib2.urlopen(request).read()

        json_results = json.loads(json_data)

        if json_results['status'] == self.STATUS_OK:
            return json_results['results']
        else:
            return None