# Function to calculate the distance between two coordinates using the Haversine formula
import math


def haversine_distance(lat2, lon2):
    r = 6371.0  # Radius of the Earth in kilometers

    # Convert degrees to radians
    lat1_rad = math.radians(32.109333)
    lon1_rad = math.radians(34.855499)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Apply Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon /
                                                                                     2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = r * c
    return distance