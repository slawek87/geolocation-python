# -*- coding: utf-8 -*-
from decimal import Decimal
from geolocation.client import ApiClient


class DistanceMatrixApiClient(ApiClient):
    """
    Client Class for Distance Matrix Google Maps Api.
    Field query_parameters has keys:
        - origins (multi origins are separated by '|')
        - destinations (multi destinations are separated by '|')
        - mode
        - avoid
    Documentation: https://developers.google.com/maps/documentation/distance-matrix/
    """
    API_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    ONE_MILE = Decimal(0.62137)  # km units
    ONE_FEET = Decimal(3.2808)
    ONE_KILOMETER = Decimal(1000.00)  # m units

    UNIT_KM = 'km'
    UNIT_M = 'm'

    MODE_DRIVING = 'driving'
    MODE_WALKING = 'walking'
    MODE_BICYCLING = 'bicycling'
    MODE_TRANSIT = 'transit'

    MODES = (
        (MODE_DRIVING, 'driving'),
        (MODE_WALKING, 'walking'),
        (MODE_BICYCLING, 'bicycling'),
        (MODE_TRANSIT, 'transit')
    )

    AVOID_TOLLS = 'tools'
    AVOID_HIGHWAYS = 'highways'
    AVOID_FERRIES = 'ferries'

    AVOIDS = (
        (AVOID_TOLLS, 'tools'),
        (AVOID_HIGHWAYS, 'highways'),
        (AVOID_FERRIES, 'ferries')
    )

    query_parameters = {}

    def __repr__(self):
        return '<DistanceMatrixApiClient: %s>' % self.api_key

    def set_query_parameters(self, origins, destinations, mode=MODE_DRIVING, avoid=None):
        """Method sets values for query_parameters."""
        def prepare_multi_params(value):
            return '|'.join(value) if isinstance(value, list) else value

        self.query_parameters['origins'] = prepare_multi_params(origins)
        self.query_parameters['destinations'] = prepare_multi_params(destinations)
        self.query_parameters['mode'] = mode

        if avoid:
            self.query_parameters['avoid'] = avoid

    def get_data(self, origins, destinations, mode=MODE_DRIVING, avoid=None):
        """Method returns json data fetched by calls from API_URL."""
        self.set_query_parameters(
            origins=origins,
            destinations=destinations,
            mode=mode,
            avoid=avoid
        )
        return self.send_data(self.API_URL, self.query_parameters)




