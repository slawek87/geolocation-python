# -*- coding: utf-8 -*-

from geolocation.api import BaseApi
from geolocation.distance_matrix import const


class DistanceMatrixApi(BaseApi):
    api ='https://maps.googleapis.com/maps/api/distancematrix/json?'
    origins_parameter = 'origins='
    destinations_parameter = 'destinations='

    modes = dict(const.MODES)

    avoids = dict(const.AVOIDS)

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

    def prepare_mode_query(self, mode):
        mode = self.modes.get(mode)

        return "mode=%s" % mode

    def prepare_avoid_query(self, avoid):
        avoid = self.avoids.get(avoid)

        return "avoid=%s" % avoid

    def prepare_query(self, origins, destinations, mode, avoid=None):
        query_ = "%s&%s&%s" % (
            self.prepare_origins_query(origins),
            self.prepare_destinations_query(destinations),
            self.prepare_mode_query(mode)
        )

        if avoid:
            query_ = "%s&%s" % (query_, self.prepare_avoid_query(avoid))

        return self.get_api_url(query_, self.api)

    def query(self, origins, destinations, mode, avoid=None):
        query_ = self.prepare_query(origins, destinations, mode, avoid)

        return self.send_request(query_)



