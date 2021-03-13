
import math
import csv


def distance(origin, destination):
    """
    Calculate the Haversine distance.
    From: https://stackoverflow.com/a/38187562/1561431

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


def closest_university(location):
    """
    Finds the closest university to location. location is a tuple
    with latitude and longitude, in that order, for the location
    you're searching from.

    This method should return a tuple with the distance and
    university name.
    """
    dist, name = 0,""
    with open('university-data.csv', newline='') as csvfile:
        csv_file = csv.DictReader(csvfile)
        for row in csv_file:
            if(row['LATITUDE']!='-' and row['LONGITUDE']!='-'):
                d = distance((float(row['LATITUDE']), float(row['LONGITUDE'])), location)
                if(dist == 0):
                    dist, name = d, row['INSTNM']
                else:
                    if(d<dist):
                        dist,name = d, row['INSTNM']
    return dist, name
