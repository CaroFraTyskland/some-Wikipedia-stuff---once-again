import math
from decimal import *


def convert_coordinates(coordinates):
    coord = Decimal(coordinates)
    hours = math.floor(coord)

    min_and_sec = (Decimal(coord) - Decimal(hours)) * 60
    minutes = math.floor(min_and_sec)

    seconds = math.floor((min_and_sec - minutes) * 60)

    return str(hours) + "/" + str(minutes) + "/" + str(seconds)
