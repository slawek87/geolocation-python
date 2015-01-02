from decimal import Decimal

ONE_MILE = Decimal(0.62137)  # km units
ONE_FEET = Decimal(3.2808)
ONE_KILOMETER = Decimal(1000.00)  # m units


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
