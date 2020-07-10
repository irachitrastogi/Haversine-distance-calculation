# ------------------------------------------------------------------------------
# Library containing the calculation for ascertaining the separation between two 
# areas on the world's surface indicated by scope and longitude.
# ------------------------------------------------------------------------------

from math import acos, cos, sin, radians

# Radius of the earth in kilometers.
erthRadKm = 6371


# A Location instance represents a position on the earth's surface. Latitude and
# longitude should be specified in degrees.
class Location:
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude


# Function to find the minimum distance between two points
# Position instances calculated using the spherical law of cosines.
# "Ref: https://en.wikipedia.org/wiki/Great-circle_distance"
def distance_cal(position1, position2):
    lat1, lon1 = radians(position1.lat), radians(position1.lon)
    lat2, lon2 = radians(position2.lat), radians(position2.lon)

    output = abs(lon1 - lon2)
    calculation = acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(output))

    return calculation * erthRadKm
