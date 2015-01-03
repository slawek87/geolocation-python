# encoding: utf-8

ONE_MILE = float(0.62137)  # km units
ONE_FEET = float(3.2808)
ONE_KILOMETER = float(1000.00)  # m units


UNIT_KM = 'km'
UNIT_M = 'm'


MODE_DRIVING = 1
MODE_WALKING = 2
MODE_BICYCLING = 3

MODES = (
    (MODE_DRIVING, 'driving'),
    (MODE_WALKING, 'walking'),
    (MODE_BICYCLING, 'bicycling')
)


AVOID_TOLLS = 1
AVOID_HIGHWAYS = 2
AVOID_FERRIES = 3

AVOIDS = (
    (AVOID_TOLLS, 'tools'),
    (AVOID_HIGHWAYS, 'highways'),
    (AVOID_FERRIES, 'ferries')
)