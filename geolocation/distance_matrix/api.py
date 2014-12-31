# -*- coding: utf-8 -*-

from geolocation.api import BaseApi


class DistanceMatrixApi(BaseApi):
    api ='https://maps.googleapis.com/maps/api/distancematrix/json?'
    origins_parameter = 'origins='
    destinations_parameter = 'destinations='

    def __repr__(self):
        return '<GoogleMatrixApi: %s>' % self.api_key

    def to_query(self, data):
        prepare = list()
        data = self.to_list(data)

        for item in data:
            prepare.append(self.join_query(item))

        return "|".join(prepare)

    def prepare_origins_query(self, origins):
        origins = self.to_query(origins)

        return "%s%s" % (self.origins_parameter, origins)

    def prepare_destinations_query(self, destinations):
        destinations = self.to_query(destinations)

        return "%s%s" % (self.destinations_parameter, destinations)

    def prepare_query(self, origins, destinations):
        query_ = "%s&%s" % (self.prepare_origins_query(origins), self.prepare_destinations_query(destinations))

        return self.get_api_url(query_, self.api)

    def query(self, origins, destinations):
        query_ = self.prepare_query(origins, destinations)
        print query_

        return self.send_request(query_)

if __name__ == "__main__":
    distance_matrix = DistanceMatrixApi('AIzaSyDNvdrZ_HEtfsuPYHV9UvZGc41BSFBolOM')
    print distance_matrix.query(['rybnik', 'oslo'], ['zagrzeb', 'oslo'])


