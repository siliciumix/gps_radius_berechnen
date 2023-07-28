# Berechnen ob eine GPS Koordinate in einem bestimmten Radius liegt

import math


def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    earth_radius = 6371000  # Earth's radius in meters
    distance = earth_radius * c

    return distance


def is_within_radius(lat1, lon1, lat2, lon2, radius):
    distance = haversine_distance(lat1, lon1, lat2, lon2)
    return distance <= radius


if __name__ == "__main__":
    # Beispielkoordinaten (Breitengrad, Längengrad) in Grad
    lat1 = 52.22657877854336
    lon1 = 8.731351135858274
    lat2 = 52.2253810475654
    lon2 = 8.730380168226874
    radius_meters = 150

    if is_within_radius(lat1, lon1, lat2, lon2, radius_meters):
        print(f"Die Koordinate liegt innerhalb des {radius_meters}-Meter-Radius.")
    else:
        print(f"Die Koordinate liegt außerhalb des {radius_meters}-Meter-Radius.")
